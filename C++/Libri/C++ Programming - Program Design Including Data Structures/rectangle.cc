//**************************************************************//
// Given the length and width of a rectangle, this C++ program  //
// computes and outputs the perimeter and area of the rectangle.//
//**************************************************************//


#include <iostream>

int main() {

	float length;
	float width;
	float area;
	float perimeter;

	length = 6.0;
	width = 4.0;

	area = length*width;
	perimeter = 2*(length+width);

	std::cout << "Perimeter = " << perimeter << std::endl;
	std::cout << "Area = " << area << std::endl; 
	
	return 0;

}
