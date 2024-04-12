<h1 align="center" id="title">SpaceWeb</h1>

![image](https://github.com/lauramejia900/Spaceweb/assets/93622576/7480016d-d907-497c-8c4d-c924635ae2e6)



<p id="description">It's an application designed for astronomy enthusiasts, providing a platform to share knowledge and engage with like-minded individuals, ranging from fellow enthusiasts to seasoned professionals in the field.</p>

## Table of Contents

- [Demo](#demo)
- [Features](#features)
- [Installation Step](#installation-steps)
- [The process](#the-process)
  - [Built with](#built-with)
- [Author](#author)

## Demo


  
## Features

Here're some of the project's best features:

*   Get a question with multi options
*   Get an automatic feedback about if the answer is correct or not
*   Track the score
*   Track the progres across the questions.

## Installation Steps:

1. Clone the repository.
2. Open the project with Xcode.
3. Run the app and enjoy it.

## The process 
### Built with

Technologies used in the project:

*   Swift 5.6
*   Xcode 13.3
*   iOS 15.5

### Quiz structure

``` Swift
// Question struct
struct Question {
  let question: String
  let answers: Array<String>
  let correctAnswer: String
  
  init(q: String, a: Array<String>, b: String){
      question = q
      answers = a
      correctAnswer = b
  }
}
```

``` Swift
// Question collection
let quiz = [
  Question(
      q: "¿Quién pintó Las meninas?",
      a: ["Francisco de Goya", "Diego Velázquez", "Salvador Dalí"],
      b: "Diego Velázquez"),
  Question(
      q: "¿Cuál es la capital de Hungría?",
      a: ["Viena", "Praga", "Budapest"],
      b: "Budapest")
]
```

## Useful resources

* [Canva](https://www.canva.com) - Used to create graphics.
* [Classes and Structures](https://docs.swift.org/swift-book/LanguageGuide/ClassesAndStructures.html) - A guide to Structures and Classes.

## License:

> This project is licensed under the MIT License

## Author

Made with 💜 by [alexcamachogz](https://twitter.com/alexcamachogz)


