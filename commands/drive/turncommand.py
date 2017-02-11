from .movecommand import MoveCommand

import subsystems
from custom.config import Config

import math


class TurnCommand(MoveCommand):
    '''Allows autonomous turning using the drive base encoders.'''

    def __init__(self, degrees, name=None):
        super().__init__(degrees, 'Turn %f degrees' % degrees)


    def initialize(self):
        '''Calculates new positions by offseting the current ones.'''

        offset = self._calculateDisplacement() * 3
        targetPositions = []
        for position in subsystems.drivetrain.getPositions():
            targetPositions.append(position + offset)

        subsystems.drivetrain.setPositions(targetPositions)


    def end(self):
        print("Successful End")
        super().end()
    def _calculateDisplacement(self):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''

        inchesPerDegree = math.pi * Config('DriveTrain/width') / 360
        totalDistanceInInches = self.distance * inchesPerDegree

        return totalDistanceInInches * Config('DriveTrain/ticksPerInch')