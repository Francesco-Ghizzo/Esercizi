//**************************************************************//
// Given the length and width of a rectangle, this C++ program  //
// computes and outputs the perimeter and area of the rectangle.//
//**************************************************************//


#include <iostream>
#include <string> 

int main(int argc, char* argv[]) {

	int length;
	int width;
	int area;
	int perimeter;

	length = std::stoi(argv[1]);
	width = std::stoi(argv[2]);

	area = length*width;
	perimeter = 2*(length+width);

	std::cout << "Perimeter = " << perimeter << std::endl;
	std::cout << "Area = " << area << std::endl; 
	
	return 0;

}
