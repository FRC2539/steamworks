from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drive.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand
from commands.pickup.pickupcommand import PickupCommand
from commands.shooter.firecommand import FireCommand
from commands.climber.climbcommand import ClimbCommand
from commands.gear.togglelightcommand import ToggleLightCommand
from commands.gear.scoregearcommand import ScoreGearCommand
from commands.test.printultrasonic import PrintUltrasonic
from commands.pickup.clearfuelcommand import ClearFuelCommand
from commands.test.getaccel import GetAccel
from commands.drive.runintowallcommand import RunIntoWallCommand

def init():
    '''
    Declare all controllers, assign axes to logical axes, and trigger
    commands on various button events. Available event types are:
        - whenPressed
        - whileHeld: cancelled when the button is released
        - whenReleased
        - toggleWhenPressed: start on first press, cancel on next
        - cancelWhenPressed: good for commands started with a different button
    '''

    mainController = LogitechDualShock(0)

    logicalaxes.driveX = mainController.LeftX
    logicalaxes.driveY = mainController.LeftY
    logicalaxes.driveRotate = mainController.RightX

    mainController.LeftTrigger.whileHeld(ClimbCommand())
    mainController.RightTrigger.toggleWhenPressed(FireCommand(Config('Shooter/speed', 11000)))
    mainController.RightBumper.whenPressed(ScoreGearCommand())
    mainController.A.toggleWhenPressed(PickupCommand())
    mainController.B.toggleWhenPressed(ClearFuelCommand())
    mainController.X.toggleWhenPressed(DriveCommand(Config('DriveTrain/preciseSpeed', 2000)))
    mainController.Y.whenPressed(GetAccel())
    mainController.Back.whenPressed(ResetCommand())
    mainController.DPadUp.whenPressed(RunIntoWallCommand(600))


    backupController = LogitechDualShock(1)

    backupController.LeftTrigger.whileHeld(ClimbCommand())
    backupController.RightTrigger.toggleWhenPressed(FireCommand(Config('Shooter/speed', 11000)))
    backupController.RightBumper.whenPressed(ScoreGearCommand())
    backupController.A.toggleWhenPressed(PickupCommand())
    backupController.B.toggleWhenPressed(ClearFuelCommand())
    backupController.X.toggleWhenPressed(DriveCommand(Config('DriveTrain/preciseSpeed', 2000)))
