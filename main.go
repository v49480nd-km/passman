package main

import(
    "fmt"
    "passman/core/utils"
)

func main() {
    var Password gen.Generate
    Password.name = "slorn"
    fmt.Println(Password.name)
}
