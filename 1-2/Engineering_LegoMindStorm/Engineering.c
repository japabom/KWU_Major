#pragma config(Sensor, S1,     Insert,         sensorEV3_Touch)
#pragma config(Sensor, S2,     Color,          sensorEV3_Color, modeEV3Color_Color)
#pragma config(Sensor, S3,     Pause,          sensorEV3_Touch)
#pragma config(Sensor, S4,     Menu,           sensorEV3_Touch)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

int coffeeSpeed=10;
int milkSpeed=10;
int waterSpeed=10;
int conveyorSpeed=30;
int coffeeTowerWait=1000;
int milkTowerWait=1000;
int waterTowerWait=1000;
int coffeeTowerAngle=90;
int milkTowerAngle=90;
int waterTowerAngle=90;

void coffeeTower(int speed,int time)  // motorA = coffeeTower
{														 // motorB = milkTower
	setMotorTarget(motorA,coffeeTowerAngle,speed);
	sleep(time);
	setMotorTarget(motorA,-coffeeTowerAngle/4,speed);	 // motorC = waterTower		 // motorD = conveyor
	sleep(time);
	setMotorTarget(motorA,coffeeTowerAngle/40,speed);
	sleep(time/2);
	motor[motorA]=0;
	sleep(2000);
}
void milkTower(int speed,int time)
{
	setMotorTarget(motorB,milkTowerAngle,speed);
	sleep(time);
	setMotorTarget(motorB,-milkTowerAngle/4,speed);
	sleep(time);
	setMotorTarget(motorB,milkTowerAngle/40,speed);
	sleep(time/2);
	motor[motorB]=0;
	sleep(2000);
}
void waterTower(int speed,int time)
{
	setMotorTarget(motorC,waterTowerAngle,speed);
	sleep(time);
	setMotorTarget(motorC,-waterTowerAngle/4,speed);
	sleep(time);
	setMotorTarget(motorC,waterTowerAngle/40,speed);
	sleep(time/2);
	motor[motorC]=0;
	sleep(2000);
}
void goConveyor(int speed)
{
	motor[motorD] = speed;
	sleep(2700);
	motor[motorD] = 0;
	sleep(2000);
}

void backConveyor(int speed)
{
	motor[motorD] = -speed;
	sleep(2700);
	motor[motorD] = 0;
	sleep(2000);
}
int selectMenu()
{
	while(true)
	{
		if(SensorValue[Color] == 1)
		{// color : Yellow 1 : Americano  Blue 3 : latte, Red 5 : Espresso
			return 1;
		}
		else if(SensorValue[Color] == 3)
		{
			return 3;
		}
		else if(SensorValue[Color] == 5)
		{
			return 5;
		}
		else
			continue;
	}
}

void pauseAlarm()
{
	playTone(800,60);

}
void finishAlarm()
{
	playTone(300,20);



}
task main()
{
	int selectedMenu;
	while(true)
	{

		while(SensorValue[Insert]==0){}
		while(SensorValue[Insert]==1){}
		if(SensorValue[Insert]==0)
		{
			playTone(500,30);
			while(SensorValue[Menu]==0){}
			if(SensorValue[Menu]==1)
			{
			selectedMenu=selectMenu();
			}

			goConveyor(conveyorSpeed);
			playTone(500,30);

			if(selectedMenu == 1)
			{
				displayCenteredBigTextLine(5,"Americano");
				coffeeTower(coffeeSpeed,coffeeTowerWait);
				waterTower(waterSpeed,waterTowerWait);
				coffeeTowerAngle+=5; // To pour same volumn next time.
				waterTowerAngle+=5;
			}
			else if(selectedMenu == 3)
			{
				displayCenteredBigTextLine(5,"Latte");
				coffeeTower(coffeeSpeed,coffeeTowerWait);
				milkTower(milkSpeed,milkTowerWait);
				coffeeTowerAngle+=5;
				milkTowerAngle+=5;
			}
			else if(selectedMenu == 5)
			{
				displayCenteredBigTextLine(5,"Espresso");
				coffeeTower(coffeeSpeed,coffeeTowerWait);

				coffeeTowerAngle+=5;
			}
			backConveyor(conveyorSpeed);
			finishAlarm();
		}

	}


}


// revise list : pauseAlarm , finishAlarm , coffeeSpeed, milkSpeed, waterSpeed, conveyorSpeed, conwaitTime, towerWaitTime, MenuAlarm, initial TowerSpeed