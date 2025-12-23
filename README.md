# `lazy-loading`

`lazy-loading` is a simple lazy module loader for python.

## Usage:
First, you'll need to `import lazy-loading`.

To lazily load a package, use:
```python
lazy-loading.lazyload("package")
```
This will inject "package" into your global variables, meaning you can use package like usual.
> [!TIP]
> If you don't want to inject into globals, you can set the `inject` parameter as such:
> ```python
> package = lazy-loading.lazyload("package", False)
> ```
> `lazyload` will return the same `LazyModule` object it would inject into your global variables.
> > Note:
> > lazyload will return the object even if `inject` is `True`.

You can lazily load submodules of your package:
```python
lazy-loading.lazyload("mypacakge.submodule")
```
> [!IMPORTANT]
> Relative imports (e.g. `.submodule`) are **not** supported. You need to use absolute module paths.

### IDE autocompletion & type-checking
To get type-checking and autocompletion, you need to import all lazy-loaded packages
if `typing.TYPE_CHECKING` is `True`:
```python
from lazy-loading import lazyload
from typing import TYPE_CHECKING

lazyload("package1")
lazyload("package2")

if TYPE_CHECKING:
    import package1
    import package2
```
This will only run if a type-checker or linter is checking your code and will not cause packages to not lazy load in normal contexts.

## Limitations:
### Partial lazy loading
Partial lazy loading (e.g. `from package import symbol`) is not supported.
Accessing an attribute or function will automatically import the entire module.

### Relative imports
As mentioned previously, relative imports are not supported.
You can lazy-load modules in your script's directory:
```python
lazy-loading.lazyload("module")
```
If you are building a package:
```
lazy-loading.lazyload("package.module")
```

### Lazily-loaded module dependencies
Imports called by lazily-loaded modules will not be lazy-loaded (unless the module uses lazy loading itself.)

### Global name injection
In unusual contexts, global name injection may fail.
To prevent this, you can assign the returned value of `lazyload` to a variable and possibly disable injection.
