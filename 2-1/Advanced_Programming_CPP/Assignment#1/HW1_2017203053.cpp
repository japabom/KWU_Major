/*
	Advanced Programming - Assignment #1

	Affiliation : Department of Computer Software
	Student ID : 2017203053
	Student Name : Hyoung Seok Kim
	
	Submission date : 2019.4.5
*/

#include "std_lib_facilities.h"

int main() 
try{
	vector<int> answers;// save the numbers of answer.
	vector<int> guesses;// save the numbers that you guessed.
	int answer;			// for appending element of answers.
	int guess;			// for appending element of your guesses.
	int opportunity=0;	// for counting your left chances.
	int num_check;		// for checking redundancy.
	char play_again;	// for asking whether you keep play game or not.
	int bull=0, cow=0;	// for counting bull and cow.

	// Creating 4 int randomly
	do {
		do {
			num_check = 0;
			if (answers.size() == 0) {
				answer = randint(9);
				answers.push_back(answer);
			}
			else if (answers.size() > 0) {
				answer = randint(9);
				for(int j = 0; j < answers.size(); j++) {
					if (answer == answers[j]) {
						num_check = 1;
						break;
					}
					else
						continue;
				}
				if(num_check==0)
					answers.push_back(answer);
			}
		} while (answers.size() < 4);

		// Guessing
		opportunity = 0;
		bull = 0;
		cow = 0;
		while (bull < 4 && opportunity < 10) {
			
			opportunity += 1;
			bull = 0;
			cow = 0;
			guesses.clear();
			cout << "Guess four numbers: ";
			for (int i = 0; i < 4; i++) {
				cin >> guess;
				if (guess < 0 || guess>9) {
					error("Out of range!");
					return 0;
				}
				guesses.push_back(guess);
			}
			for (int i = 0; i < 4; i++) {
				if (answers[i] == guesses[i])
					bull += 1;
			}
			
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					if (i != j && answers[i] == guesses[j])
						cow += 1;
				}
			}
			// Distinguish between plural or singular.
			if (bull == 1) 
				cout << bull << " bull ";
			else if(bull > 1) 
				cout << bull << " bulls ";

			if (bull != 0 && cow != 0)
				cout << "and ";

			if (cow == 1)
				cout << cow << " cow";
			else if (cow > 1)
				cout << cow << " cows";

			if (bull == 0 && cow == 0) {
				cout << "All your guesses are wrong.";
			}
			cout << '.' << endl;

			if (bull == 4)
				cout << "Congratulations!" << endl;

			// if you used all chances. you failed.
			switch (opportunity) {
			case 10:
				cout << "You failed!" << endl;
				cout << "Correct numbers are: ";
				for (int j = 0; j < answers.size(); j++)
					cout << answers[j] << ' ';
				break;
			default:
				continue;
			}
			cout << endl;
		}
		// for asking whether you keep play game or not.
		cout<<"Play again? (y/n) ";
		cin >> play_again;
		if (play_again != 'y' && play_again != 'n') {
			error("Wrong input!");
			return 0;
		}
		answers.clear(); // for creating 4 new answers.
	}while(play_again=='y'); // if you input 'y', new game start.

	keep_window_open();	
}
catch (runtime_error& e) { 
	cout << e.what() << endl;
	keep_window_open();
}
catch (...) {
	cerr << "exception" << endl;
	keep_window_open();
}

