def setup(): 
    global playerX, playerY, sprite, frontFace, backRun, firstR, secR, triR, fourR, fiveR, sixR, sevR, eightR, nineR
    size(800,800)
    background(255)
    frontFace = loadImage("Stand.gif")
    backRun = loadImage("back.gif")
    firstR= loadImage("1run.gif")
    secR= loadImage("2run.gif")
    triR= loadImage("3run.gif")
    fourR= loadImage("4run.gif")
    fiveR= loadImage("5run.gif")
    sixR= loadImage("6run.gif")
    sevR= loadImage("7run.gif")
    eightR= loadImage("8run.gif")
    nineR= loadImage("9run.gif")
    sprite = frontFace
    playerX = 250
    playerY = 250
    
    image(sprite,playerX, playerY, 50, 50)
    playerMiddleX = playerX + 12
    playerMiddleY = playerY + 12
    
    
    
    if (keyPressed):
        if (key == 'DOWN'):
            sprite = frontFace
            
        elif(key == 'RIGHT'):
            sprite = firstR, secR, triR, fourR, fiveR, sixR, sevR, eightR, nineR
            
     
            
        
