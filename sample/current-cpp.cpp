class Ball
{
private:
	int x;
	int y;
public:
	Ball() {
		x = 0;
		y = 0;
	}
	Ball(int xc, int yc) {
		if(isInLimit(xc)) {
			x = xc;
		}
		if (isInLimit(yc)) {
			y = yc;
		}
	}
	bool isInLimit(int a) {
		return (a >= 0 && a < 100);
	}
	void Move(int x_delta, int y_delta) {
		x += x_delta;
		y += y_delta;
	}
	void MoveALittle() {
		x += 1;
		y += 1;
	}
};
