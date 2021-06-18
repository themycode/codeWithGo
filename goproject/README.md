### go 使用

初始化项目module: go mod init goproject

添加依赖项: go mod edit -require github.com/labstack/echo

拉取依赖项：go get ,然后go run就可以执行

### 本地不在同一级目录下的包使用

1. 定义目录和代码文件package mypackage，并开发代码功能
2. 查看go.mod中定义的module，module gomodule
3. 在main中的import中添加引入模块`gomodule/mypackage`，然后就可以调用代码执行 `mypackage.New()`

### 不在同一个目录下的引入

目录结构如下，两个不同的项目包

```txt
├── moduledemo
│   ├── go.mod
│   └── main.go
└── mypackage
    ├── go.mod
    └── mypackage.go
```

导入包:这个时候，`mypackage`也需要进行module初始化，即拥有一个属于自己的go.mod 文件，内容如下：

```mod
module mypackage

go 1.16
```

然后我们在`moduledemo/main.go`中按如下方式导入：

```go
import (
 "fmt"
 "mypackage"
)
func main() {
 mypackage.New()
 fmt.Println("main")
}
```

因为这两个包不在同一个项目路径下，你想要导入本地包，并且这些包也没有发布到远程的github或其他代码
仓库地址。这个时候我们就需要在go.mod文件中使用replace指令。

在调用方也就是moduledemo/go.mod中按如下方式指定使用相对路径来寻找mypackage这个包。

```mod
module moduledemo

go 1.14


require "mypackage" v0.0.0
replace "mypackage" => "../mypackage"
```

被导入的包的代码如下：

```go
package godemo

import (
 "fmt"
)

// New is test!
func New() {
 fmt.Println("hello world")
}
```
