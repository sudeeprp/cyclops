class Ball
{
private:
	int x;
	int y;
public:
	Ball()
	{
		x = 0;
		y = 0;
	}
	Ball(int xc, int yc)
	{
		if(xc >= 0 && xc < 100) {
			x = xc;
		}
		if (yc >= 0 && yc < 100) {
			y = yc;
		}
	}
	void Move(int x_delta, int y_delta)
	{
		x += x_delta;
		y += y_delta;
	}
};
