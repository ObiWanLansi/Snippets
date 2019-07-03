 
size(800, 600, P3D); 
background(0);
lights();

noStroke();
pushMatrix();
translate(130, height/2, 0);
rotateY(1.25);
rotateX(-0.4);
box(100);
popMatrix();

noFill();
stroke(255);
pushMatrix();
translate(500, height*0.35, -200);
sphere(280);
popMatrix();