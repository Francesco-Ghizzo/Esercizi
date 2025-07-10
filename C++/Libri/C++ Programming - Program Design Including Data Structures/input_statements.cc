// This program illustrates how input statements work


#include <iostream>


int main() {

	int length;
	int width;
	int area;
	int perimeter;

	std::cout << "Length:";
	std::cin >> length;
	std::cout << "Width:";
	std::cin >> width;

	area = length*width;
	perimeter = 2*(length+width);

	std::cout << "Perimeter = " << perimeter << std::endl;
	std::cout << "Area = " << area << std::endl; 
	
	return 0;

}
