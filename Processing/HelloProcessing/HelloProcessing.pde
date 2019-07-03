void setup() {
  size(800, 600);
}


void draw() {
  
  background(0);

  stroke(0xA0, 0xA0, 0xA0);
  
  for(int x=0;x<width;x+=20) {
      line(x,0,x,height);
  }
  
  for(int y=0;y<height;y+=20) {
      line(0,y,width,y);
  }

  stroke(50, 255, 50);

  line(0, mouseY, width, mouseY);
  line(mouseX, 0, mouseX, height);
}

