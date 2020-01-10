/*
	Advanced Programming - Assignment #3 Cellular_Automata

	Affiliation : Department of Computer Software
	Student ID : 2017203053
	Student Name : Hyoung Seok Kim

	Submission date : 2019. 6. 6
*/
#include "Graph.h"
#include <ctime>
#include "HW3.h"

BinaryBitmap::BinaryBitmap(int w, int h) {
	height = new int(h);
	width = new int(w);
	map = new bool*[h];
	for (int i = 0; i < h; i++) {
		map[i] = new bool[w];
	}
	clear();

}
BinaryBitmap::~BinaryBitmap() {
	delete width;
	delete height;
	for (int i = 0; i < getHeight(); i++) {
		delete[] map[i];
	}
	delete[] map;
}
void BinaryBitmap::clear() {
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			set(i, j, false);
		}
	}
}
bool BinaryBitmap::get(int x, int y) const {
	if (x >= getWidth() || y >= getHeight() || x < 0 || y < 0)
		return false;

	return map[y][x];
}
void BinaryBitmap::set(int x, int y, bool v) {
	if (x >= getWidth() || y >= getHeight() || x < 0 || y < 0)
		return;

	map[y][x] = v;
}
int BinaryBitmap::getWidth() const {
	return *width;
}
int BinaryBitmap::getHeight() const {
	return *height;
}

BinaryBitmap::BinaryBitmap(const BinaryBitmap& bb) {
	this->width = new int(*bb.width);
	this->height = new int(*bb.height);
	this->map = new bool*[getWidth()];
	for (int i = 0; i < this->getWidth(); i++) {
		this->map[i] = new bool[this->getHeight()];
	}
	for (int i = 0; i < this->getWidth(); i++) {
		for (int j = 0; j < this->getHeight(); j++) {
			this->map[i][j] = bb.map[i][j];
		}
	}
}
// copy constructor
BinaryBitmap& BinaryBitmap::operator=(const BinaryBitmap& bb) {
	if (this->width != bb.width || this->height != bb.height) {
		delete[] this->width;
		delete[] this->height;
		for (int i = 0; i < *bb.width; i++) {
			delete[] this->map[i];
		}
		delete this->map;
		this->width = new int(*bb.width);
		this->height = new int(*bb.height);
		this->map = new bool*[getHeight()];
		for (int i = 0; i < getHeight(); i++)
			this->map[i] = new bool[getWidth()];
		for (int i = 0; i < this->getWidth(); i++) {
			for (int j = 0; j < this->getHeight(); j++) {
				this->map[i][j] = bb.map[i][j];
			}
		}
	}
	else {
		this->width = bb.width;
		this->height = bb.height;
		for (int i = 0; i < this->getWidth(); i++) {
			for (int j = 0; j < this->getHeight(); j++) {
				this->map[i][j] = bb.map[i][j];
			}
		}
	}

	return *this;
}

CellularAutomata::CellularAutomata(int w, int h) {
	bitmap = new BinaryBitmap(w, h);
}
CellularAutomata::~CellularAutomata() {
	delete bitmap;
}
void CellularAutomata::initialize(InitType t) {
	srand((unsigned int)time(0));
	int per;
	switch (t) {
	case InitType::CLEAN:
		clear();
		break;
	case InitType::RANDOM:
		clear();
		for (int i = 0; i < getWidth(); i++) {
			for (int j = 0; j < getHeight(); j++) {
				per = rand() % 2;
				if (per % 2 == 0)
					set(i, j, true);
				else
					set(i, j, false);
			}
		}
		break;
	case InitType::BEEHIVE:
		clear();
		set(getWidth() / 2 - 2, getHeight() / 2 - 1, true);
		set(getWidth() / 2 + 1, getHeight() / 2 - 1, true);
		set(getWidth() / 2 - 1, getHeight() / 2 - 2, true);
		set(getWidth() / 2, getHeight() / 2 - 2, true);
		set(getWidth() / 2 - 1, getHeight() / 2, true);
		set(getWidth() / 2, getHeight() / 2, true);

		break;
	case InitType::GLIDER:
		clear();
		set(getWidth() / 2 - 1, getHeight() / 2 - 2, true);
		set(getWidth() / 2 + 1, getHeight() / 2 - 2, true);
		set(getWidth() / 2, getHeight() / 2 - 1, true);
		set(getWidth() / 2 + 1, getHeight() / 2 - 1, true);
		set(getWidth() / 2, getHeight() / 2, true);
		break;
	case InitType::OSCILLATOR:
		clear();
		set(getWidth() / 2 - 17, getHeight() / 2, true); // left square
		set(getWidth() / 2 - 16, getHeight() / 2, true);
		set(getWidth() / 2 - 17, getHeight() / 2 + 1, true);
		set(getWidth() / 2 - 16, getHeight() / 2 + 1, true);

		set(getWidth() / 2 + 17, getHeight() / 2 - 1, true); // right square
		set(getWidth() / 2 + 18, getHeight() / 2 - 1, true);
		set(getWidth() / 2 + 17, getHeight() / 2 - 2, true);
		set(getWidth() / 2 + 18, getHeight() / 2 - 2, true);

		set(getWidth() / 2, getHeight() / 2 + 1, true); // left mid
		set(getWidth() / 2 - 1, getHeight() / 2 + 1, true);
		set(getWidth() / 2 - 1, getHeight() / 2, true);
		set(getWidth() / 2 - 1, getHeight() / 2 + 2, true);
		set(getWidth() / 2 - 2, getHeight() / 2 + 3, true);
		set(getWidth() / 2 - 2, getHeight() / 2 - 1, true);
		set(getWidth() / 2 - 3, getHeight() / 2 + 1, true);
		set(getWidth() / 2 - 4, getHeight() / 2 - 2, true);
		set(getWidth() / 2 - 5, getHeight() / 2 - 2, true);
		set(getWidth() / 2 - 4, getHeight() / 2 + 4, true);
		set(getWidth() / 2 - 5, getHeight() / 2 + 4, true);
		set(getWidth() / 2 - 6, getHeight() / 2 - 1, true);
		set(getWidth() / 2 - 6, getHeight() / 2 + 3, true);
		set(getWidth() / 2 - 7, getHeight() / 2, true);
		set(getWidth() / 2 - 7, getHeight() / 2 + 1, true);
		set(getWidth() / 2 - 7, getHeight() / 2 + 2, true);

		set(getWidth() / 2 + 3, getHeight() / 2, true);// right mid
		set(getWidth() / 2 + 3, getHeight() / 2 - 1, true);
		set(getWidth() / 2 + 3, getHeight() / 2 - 2, true);
		set(getWidth() / 2 + 4, getHeight() / 2, true);
		set(getWidth() / 2 + 4, getHeight() / 2 - 1, true);
		set(getWidth() / 2 + 4, getHeight() / 2 - 2, true);
		set(getWidth() / 2 + 5, getHeight() / 2 + 1, true);
		set(getWidth() / 2 + 5, getHeight() / 2 - 3, true);
		set(getWidth() / 2 + 7, getHeight() / 2 + 1, true);
		set(getWidth() / 2 + 7, getHeight() / 2 + 2, true);
		set(getWidth() / 2 + 7, getHeight() / 2 - 3, true);
		set(getWidth() / 2 + 7, getHeight() / 2 - 4, true);
		break;

	}
}
void CellularAutomata::clear() {
	bitmap->clear();
}
void CellularAutomata::resize(int w, int h) {
	tempmap = new bool*[getHeight()];
	int* tempwidth = new int(getWidth());
	int* tempheight = new int(getHeight());
	for (int i = 0; i < getHeight(); i++) {
		tempmap[i] = new bool[getWidth()];
	}
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			tempmap[i][j] = bitmap->map[i][j];
		}
	}
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			bitmap->map[i][j] = tempmap[i][j];
		}
	}
	delete bitmap;
	bitmap = new BinaryBitmap(w, h);
	clear();
	if (*tempheight < getHeight()) {
		for (int i = 0; i < *tempheight; i++) {
			for (int j = 0; j < *tempwidth; j++) {
				bitmap->map[getHeight() / 2 - (*tempheight) / 2 + i][getWidth() / 2 - (*tempwidth) / 2 + j] = tempmap[i][j];
			}
		}
	}
	else {
		for (int i = 0; i < getHeight(); i++) {
			for (int j = 0; j < getWidth(); j++) {
				bitmap->map[i][j] = tempmap[*tempheight / 2 - getHeight() / 2 + i][*tempwidth / 2 - getWidth() / 2 + j];
			}
		}
	}

	for (int i = 0; i < *tempheight; i++)
		delete[] tempmap[i];
	delete[] tempmap;
	delete[] tempwidth;
	delete[] tempheight;
} // 사이즈 바뀌었을 때 동작
bool CellularAutomata::copy(const CellularAutomata* automata) {
	if (bitmap->getWidth() != automata->getWidth() || bitmap->getHeight() != automata->getHeight()) {
		return false;
	}
	*bitmap = *automata->bitmap;
}

void CellularAutomata::set(int x, int y, bool v) {
	bitmap->set(x, y, v);
}
bool CellularAutomata::get(int x, int y) const {
	bool a = bitmap->get(x, y);
	return a;
}

int CellularAutomata::getWidth() const {
	return bitmap->getWidth();
}
int CellularAutomata::getHeight() const {
	return bitmap->getHeight();
}

LifeAutomata::LifeAutomata(int w, int h) : CellularAutomata(w, h) { }

SeedAutomata::SeedAutomata(int w, int h) : CellularAutomata(w, h) { }

ReplicatorAutomata::ReplicatorAutomata(int w, int h) : CellularAutomata(w, h) { }

void LifeAutomata::update() {
	tempmap = new bool*[getHeight()];
	for (int i = 0; i < getHeight(); i++) {
		tempmap[i] = new bool[getWidth()];
	}
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			tempmap[i][j] = bitmap->map[i][j];
		}
	}

	int black_check;
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			black_check = 0;
			for (int k = i - 1; k <= i + 1; k++) {
				for (int s = j - 1; s <= j + 1; s++) {
					if (k < 0 || s < 0 || k >= getHeight() - 1 || s >= getWidth() - 1) {}
					else if (k == i && s == j)
						continue;
					else if (bitmap->map[k][s] == true)
						black_check += 1;
					else
						continue;

				}
			}
			if (tempmap[i][j] == true && black_check < 2)
				tempmap[i][j] = false;
			else if (tempmap[i][j] == true && black_check == 2)
				tempmap[i][j] = true;
			else if (tempmap[i][j] == true && black_check == 3)
				tempmap[i][j] = true;
			else if (tempmap[i][j] == true && black_check > 3)
				tempmap[i][j] = false;
			else if (tempmap[i][j] == false && black_check == 3) // revive
				tempmap[i][j] = true;
			else
				tempmap[i][j] = false;
		}
	}
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			bitmap->map[i][j] = tempmap[i][j];
		}
	}
	for (int i = 0; i < getHeight(); i++)
		delete[] tempmap[i];
	delete[] tempmap;

}

void SeedAutomata::update() {
	tempmap = new bool*[getHeight()];
	for (int i = 0; i < getHeight(); i++) {
		tempmap[i] = new bool[getWidth()];
	}
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			tempmap[i][j] = bitmap->map[i][j];
		}
	}

	int black_check;
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			black_check = 0;
			for (int k = i - 1; k <= i + 1; k++) {
				for (int s = j - 1; s <= j + 1; s++) {
					if (k < 0 || s < 0 || k >= getHeight() - 1 || s >= getWidth() - 1) {}
					else if (k == i && s == j)
						continue;
					else if (bitmap->map[k][s] == true)
						black_check += 1;
					else
						continue;

				}
			}
			if (tempmap[i][j] == false && black_check == 2) // revive
				tempmap[i][j] = true;
			else
				tempmap[i][j] = false;
		}
	}
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			bitmap->map[i][j] = tempmap[i][j];
		}
	}
	for (int i = 0; i < getHeight(); i++)
		delete[] tempmap[i];
	delete[] tempmap;

}
void ReplicatorAutomata::update() {
	tempmap = new bool*[getHeight()];
	for (int i = 0; i < getHeight(); i++) {
		tempmap[i] = new bool[getWidth()];
	}
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			tempmap[i][j] = bitmap->map[i][j];
		}
	}

	int black_check;
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			black_check = 0;
			for (int k = i - 1; k <= i + 1; k++) {
				for (int s = j - 1; s <= j + 1; s++) {
					if (k < 0 || s < 0 || k >= getHeight() - 1 || s >= getWidth() - 1) {}
					else if (k == i && s == j)
						continue;
					else if (bitmap->map[k][s] == true)
						black_check += 1;
					else
						continue;

				}
			}

			if (tempmap[i][j] == true && black_check == 1)
				tempmap[i][j] = true;
			else if (tempmap[i][j] == true && black_check == 3)
				tempmap[i][j] = true;
			else if (tempmap[i][j] == true && black_check == 5)
				tempmap[i][j] = true;
			else if (tempmap[i][j] == true && black_check == 7)
				tempmap[i][j] = true;
			else if (tempmap[i][j] == true && black_check == 2)
				tempmap[i][j] = false;
			else if (tempmap[i][j] == true && black_check == 4)
				tempmap[i][j] = false;
			else if (tempmap[i][j] == true && black_check == 6)
				tempmap[i][j] = false;
			else if (tempmap[i][j] == true && black_check == 8)
				tempmap[i][j] = false;
			else if (tempmap[i][j] == true && black_check == 0)
				tempmap[i][j] = false;
			else if (tempmap[i][j] == false && black_check == 1) // revive
				tempmap[i][j] = true;
			else if (tempmap[i][j] == false && black_check == 3) // revive
				tempmap[i][j] = true;
			else if (tempmap[i][j] == false && black_check == 5) // revive
				tempmap[i][j] = true;
			else if (tempmap[i][j] == false && black_check == 7) // revive
				tempmap[i][j] = true;
			else
				tempmap[i][j] = false;
		}
	}
	for (int i = 0; i < getHeight(); i++) {
		for (int j = 0; j < getWidth(); j++) {
			bitmap->map[i][j] = tempmap[i][j];
		}
	}
	for (int i = 0; i < getHeight(); i++)
		delete[] tempmap[i];
	delete[] tempmap;

}
