#include <iostream>
#include <stdio.h>

#include "include/ok.h"

int main() {
  std::cout << "Hello World!" << std::endl;
  std::cout << dummy_helper::add_bye_string("Good");
  return 0;
}
