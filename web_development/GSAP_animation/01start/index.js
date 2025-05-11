// use a class or ID
gsap.to(".box", { x: 200 });

// a complex CSS selector
gsap.to("section > .box", { x: 200 });

// a variable
let box = document.querySelector(".box");
gsap.to(box, { x: 200 })

// or even an Array of elements
let square = document.querySelector(".square");
let circle = document.querySelector(".circle");
                                      
gsap.to([square, circle], { x: 200 })

gsap.to(target, {
  // this is the vars object
  // it contains properties to animate
  x: 200,
  rotation: 360,
  // and special properties
  duration: 12
})