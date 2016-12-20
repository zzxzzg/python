#! /usr/bin/env python3
#当其他模块 调用  from package1 import * 的时候会自动包含所有__all__中定义的模块,如果包提供者更新了包，那么应该及时更新__all__的内容
__all__ = ["module_test3"]