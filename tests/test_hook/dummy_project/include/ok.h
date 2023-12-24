#pragma once

#include <math.h>
#include <string>

namespace dummy_helper {
std::string add_bye_string(const std::string& input)
   {
      const std::string bye_string{"bye"};
      return input + bye_string;
   }
}  // namespace dummy_helper
