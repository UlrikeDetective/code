// use a class or ID
gsap.to(".box", { x: 200 });

// a complex CSS selector
gsap.to("section > .box", { x: 200 });

// a variable
let box = document.querySelector(".box");
gsap.to(box, { x: 200 })

// Select elements
let square = document.querySelector(".square");
let circle = document.querySelector(".circle");

// Animate both square and circle horizontally
if (square && circle) {
  gsap.to([square, circle], { x: 200 });
}

// Animate the circle to transform into a circle shape
if (circle) {
  gsap.to(".circle", { x: 200, borderRadius: "50%" });
}

gsap.to(target, {
  // this is the vars object
  // it contains properties to animate
  x: 200,
  rotation: 360,
  // and special properties
  duration: 12
});