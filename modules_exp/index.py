import mod_ios  # 1 импорт модуля из этой же директории
from folder_external_module import mod_android  # 2 импорт модуля из вложеной директории
from folder_external_module.mod_android import android, printing  # 3 импорт переменных из директории
import script_1  # 4
from script_1 import var_1  # 5
import script_2  # 6


print(mod_ios.ios)  # 1
mod_ios.printing()

print(mod_android.android)  # 2
mod_android.printing()

print(android)  # 3 так как переменные импортированы то мы используем их без префикса
printing()

print(script_1.var_1)  # 4
print(var_1)  # 5

