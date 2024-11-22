var cvs = document.getElementById("canvas");
var ctx = cvs.getContext("2d");

// Load images
var bird = new Image();
var bg = new Image();
var fg = new Image();
var pipeNorth = new Image();
var pipeSouth = new Image();

bird.src = "images/bird.png";
bg.src = "images/bg.png";
fg.src = "images/fg.png";
pipeNorth.src = "images/pipeNorth.png";
pipeSouth.src = "images/pipeSouth.png";

// Game settings
var gap = 100;
var constant;

var bX =100;
var bY = 150;

// Adjust gravity and pipe speed
var gravity = 0.75; // Reduced gravity for slower falling
var pipeSpeed = 0.5; // Reduced speed for pipes

var score = 0;
var isGameOver = false;

// Audio files
var fly = new Audio();
var scor = new Audio();
var bgMusic = new Audio();
fly.src = "sounds/fly.mp3";
scor.src = "sounds/score.mp3";
bgMusic.src = "sounds/background.mp3"; // Add background music file

// Start background music
bgMusic.loop = true;
bgMusic.play();

// On key down
document.addEventListener("keydown", moveUp);
document.addEventListener("touchstart", moveUp); // Mobile controls

function moveUp() {
    if (!isGameOver) {
        bY -= 25; // Jump height
        fly.play();
    }
}

// Pipe coordinates
var pipe = [];
pipe[0] = {
    x: cvs.width,
    y: 0
};

// Draw images
function draw() {
    ctx.drawImage(bg, 0, 0);
    
    for (var i = 0; i < pipe.length; i++) {
        constant = pipeNorth.height + gap;
        ctx.drawImage(pipeNorth, pipe[i].x, pipe[i].y);
        ctx.drawImage(pipeSouth, pipe[i].x, pipe[i].y + constant);
        
        // Move pipes according to the adjusted speed
        pipe[i].x -= pipeSpeed;

        if (pipe[i].x == 125) {
            pipe.push({
                x: cvs.width,
                y: Math.floor(Math.random() * pipeNorth.height) - pipeNorth.height
            });
        }

        // Detect collision
        if (bX + bird.width >= pipe[i].x && bX <= pipe[i].x + pipeNorth.width && 
            (bY <= pipe[i].y + pipeNorth.height || bY + bird.height >= pipe[i].y + constant) || 
            bY + bird.height >= cvs.height - fg.height) {
            gameOver(); // Call game over function
        }

        if (pipe[i].x == 5) {
            score++;
            scor.play();
        }
    }

    // Boundary check for the bird
    if (bY + bird.height >= cvs.height - fg.height) {
        bY = cvs.height - fg.height - bird.height; // Prevent going below the ground
        gameOver(); // Call game over function
    }
    
    if (bY < 0) {
        bY = 0; // Prevent going above the top
    }

    ctx.drawImage(fg, 0, cvs.height - fg.height);
    ctx.drawImage(bird, bX, bY);
    
    // Apply gravity to the bird's position
    bY += gravity;

    ctx.fillStyle = "#000";
    ctx.font = "20px Verdana";
    ctx.fillText("Score : " + score, 10, cvs.height - 20);

    if (!isGameOver) {
        requestAnimationFrame(draw);
    }
}

function gameOver() {
    isGameOver = true;
    bgMusic.pause(); // Stop background music
    document.getElementById("finalScore").innerText = "Your Score: " + score;
    document.getElementById("gameOver").style.display = "block"; // Show game over screen
}

function restartGame() {
    isGameOver = false;
    score = 0;
    bY = 150; // Reset bird position
    pipe = [];
    pipe[0] = { x: cvs.width, y: 0 };
    
    document.getElementById("gameOver").style.display = "none"; // Hide game over screen
    bgMusic.currentTime = 0; // Reset background music to start
    bgMusic.play(); // Restart background music
    
    draw(); // Restart drawing the game
}

// Start the game loop
draw();