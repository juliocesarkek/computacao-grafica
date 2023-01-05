function setup() {
    createCanvas(400, 400);
    background("#e5e5e5");
}

function draw() {
    push();
    translate(width * 0.5, height * 0.5);
    bezierCurve([[-100, 0], [-140, -100], [100, -120], [160, 0]], 0.01, "#dc2626");
    pop();
}

function bezierCurve(controlPoints, ratio, color) {
    const lerp = (t, p1, p2) => (1 - t) * p1 + t * p2;

    const reduce = (t, p1, p2, ...ps) => ps.length > 0
        ? [lerp(t, p1, p2), ...reduce(t, p2, ...ps)]
        : [lerp(t, p1, p2)];

    const deCasteljau = (t, ps) => ps.length > 1
        ? deCasteljau(t, reduce(t, ...ps))
        : ps[0];

    const formatControlPoints = function (cps) {
        let result = {
            x: [],
            y: []
        };
        for (cp of cps) {
            result.x.push(cp[0]);
            result.y.push(cp[1]);
        }
        return result;
    };

    const formatedCP = formatControlPoints(controlPoints);

    beginShape(CURVE);
    stroke(color);
    fill("#e5e5e5");
    for (let goalRatio = 0; goalRatio <= 1; goalRatio += ratio) {
        let x = deCasteljau(goalRatio, formatedCP.x);
        let y = deCasteljau(goalRatio, formatedCP.y);
        vertex(x, y);
    }
    endShape();
}