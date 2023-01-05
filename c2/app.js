function setup() {
    createCanvas(400, 400);
    background("#e5e5e5");
}

function draw() {
    push();
    translate(width * 0.5, height * 0.5);
    star(0, 0, 40, 70, 5, "#dc2626");
    pop();
}

function star(x, y, radius1, radius2, npoints, color) {
    let angle = TWO_PI / npoints;
    let halfAngle = angle / 2.0;
    beginShape();
    noStroke();
    fill(color);
    for (let a = 0; a < TWO_PI; a += angle) {
        let sx = x + cos(a) * radius2;
        let sy = y + sin(a) * radius2;
        vertex(sx, sy);
        sx = x + cos(a + halfAngle) * radius1;
        sy = y + sin(a + halfAngle) * radius1;
        vertex(sx, sy);
    }
    endShape(CLOSE);
}
