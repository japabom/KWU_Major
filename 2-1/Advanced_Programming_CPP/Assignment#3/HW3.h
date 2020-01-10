/*
	Advanced Programming - Assignment #3 Cellular_Automata

	Affiliation : Department of Computer Software
	Student ID : 2017203053
	Student Name : Hyoung Seok Kim

	Submission date : 2019. 6. 6
*/
#include "Graph.h"
#include <ctime>

class BinaryBitmap {
private:
	int *width;
	int *height;
public:
	bool** map;

	BinaryBitmap(int w, int h); // constructor
	~BinaryBitmap();  // destructor

	BinaryBitmap(const BinaryBitmap& bb); // copy constructor 
	BinaryBitmap& operator=(const BinaryBitmap& bb);

	void clear();

	bool get(int x, int y) const;
	void set(int x, int y, bool v);

	int getWidth() const;
	int getHeight() const;



};
class CellularAutomata {
public:
	enum class InitType { CLEAN, RANDOM, BEEHIVE, GLIDER, OSCILLATOR };

	CellularAutomata(int w, int h); // constructor
	virtual ~CellularAutomata(); // destructor

	void initialize(InitType t);
	void clear();
	void resize(int w, int h);
	bool copy(const CellularAutomata* automata);

	virtual void update() {
		return;
	};

	void set(int x, int y, bool v);
	bool get(int x, int y) const;

	int getWidth() const;
	int getHeight() const;

	
protected:
	bool** tempmap;
	BinaryBitmap *bitmap;
};
class LifeAutomata : public CellularAutomata {
public:
	LifeAutomata(int w, int h);
	void update() override;
};
class SeedAutomata : public CellularAutomata {
public:
	SeedAutomata(int w, int h);
	void update() override;
protected:
	bool** tempmap;
};
class ReplicatorAutomata : public CellularAutomata {
public:
	ReplicatorAutomata(int w, int h);
	void update() override;
protected:
	bool** tempmap;
};


