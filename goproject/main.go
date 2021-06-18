package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
	// 引入同一个项目不同目录包
	"gomodule/mypackage"
	// 引入不同项目包
	"godemo"
)

func main() {
	mypackage.New()
	godemo.New()
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		s := "go test!!!"
		return c.String(http.StatusOK, "Hello, World!"+s)
	})
	e.Logger.Fatal(e.Start(":1323"))
}
