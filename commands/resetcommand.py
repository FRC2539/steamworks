from wpilib.command import InstantCommand

import subsystems

class ResetCommand(InstantCommand):
    '''
    Disable any running commands for all subsystems, except Monitor. This should
    be used to stop any motion and return the commands to a safe state. In
    general just requiring a subsystem will stop its current command. Additional
    resetting can be handled in the initialize method.
    '''

    def __init__(self):
        '''Require all active subsystems here.'''

        super().__init__('Reset')

        self.requires(subsystems.drivetrain)
        self.requires(subsystems.climber)
        self.requires(subsystems.pickup)
        self.requires(subsystems.shooter)


    def initialize(self):
        subsystems.drivetrain.stop()
        subsystems.climber.stop()
        subsystems.pickup.stop()
        subsystems.shooter.stop()
        subsystems.feeder.close()
