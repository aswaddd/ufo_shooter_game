def setup():
    size( 600, 600)
    global bg, jet, ufo, rock, restart, exitGame, start, resume
    global startTime, gamePage, timeOn, minute, second, millisecond, totalTime
    global rockY, rockX, rockDy, rockW, rockH
    global bulletPosX, bulletPosY, bulletDy, bulletW, bulletH
    global condition, bulletVisible
    global health, score
    global totalNum, img, ufoX, ufoY, ufoDy, ufoW, ufoH
    global jetW, jetH, rockCount, ufoMissed
    global tip1X, tip2X, tip3X, tip4X, tip1Dx, tip2Dx, tip3Dx, tip4Dx
    
    #welcome page
    tip1X = random(150, 200)
    tip2X = random(50, 100)
    tip3X = random(200, 350)
    tip4X = random(200, 300)
    
    tip1Dx = random(0.8, 1.5)
    tip2Dx = random(0.8, 1.5)
    tip3Dx = random(0.8, 1.5)
    tip4Dx = random(0.8, 1.5)
    
    #images
    bg = loadImage("spacebg.png")
    jet = loadImage("jet.png")
    ufo = loadImage("ufo.png")
    rock = loadImage("rock.png")
    restart = loadImage("restart.png")
    exitGame = loadImage("exit.png")
    start = loadImage("start.png")
    resume = loadImage("resume.png")
    
    #jet
    jetW = 80
    jetH = 80
    
    #bullet
    bulletW = 15
    bulletH = 35
    condition = 0 # 0 is no bullet, 1 is visible bullet
    bulletDy = 8
    bulletPosX = []
    bulletPosY = []
    bulletVisible = []

    #rock
    rockW = 100
    rockH = 100
    rockX = random(0, width - 100)
    rockY = -100
    rockDy = int(random( 3, 8)) 
    rockCount = 0
    
    #ufo
    img = []
    ufoX = []
    ufoY = []
    ufoDy = []
    totalNum = 5
    ufoW = 80
    ufoH = 80
    ufoMissed = 0
    
    #game stuff
    gamePage = 0 #0 is welcome, 1 is main game, 2 is end page, 3 is pause page
    score = 0
    health = 3
    
    #time
    startTime = millis()
    minute = second = millisecond = 0
    timeOn = False
    totalTime = 0
    
    #ufo spawn position and speed
    for i in range(totalNum):
        img.append(loadImage("ufo" + str(i) + ".png"))
        ufoX.append(random(0, width - ufoW))
        ufoY.append(-random(0, 100))
        ufoDy.append(random(1, 5))
    
def draw():
    global gamePage
    
    image(bg, 0, 0, width, height)
    
    if(gamePage == 0):
        welcomePage()
    if(gamePage == 1):
        mainPage()
    if(health <= 0):
        gamePage = 2
    if(gamePage == 2):
        endPage()
    if(condition == 1):
        drawBullet(bulletPosX, bulletPosY)
    if(gamePage == 3):
        pausePage()
        
def welcomePage():
    global gamePage, tip1X, tip2X, tip3X, tip4X, tip1Dx, tip2Dx, tip3Dx, tip4Dx
    
    #title screen
    
    textSize(75)
    fill(255, 170, 0)
    text("UFO SHOOTER", 40, 250)
    
    #game instructions
    
    textSize(18)
    fill(255, 255, 45)
    text("Use mouse to move. Click to shoot.", tip1X, 425)
    tip1X = tip1X + tip1Dx
    if(tip1X > width - 300 or tip1X < 0):
        tip1Dx = -tip1Dx
    
    textSize(18)
    fill(255, 255, 45)
    text("Shoot the UFOs!!", tip2X, 525)
    tip2X = tip2X - tip2Dx
    if(tip2X > width - 150 or tip2X < 0):
        tip2Dx = -tip2Dx
    
    textSize(18)
    fill(255, 255, 45)
    text("Avoid the Asteriods!!!", tip3X, 560)
    tip3X = tip3X + tip3Dx
    if(tip3X > width - 200 or tip3X < 0):
        tip3Dx = -tip3Dx
        
    textSize(18)
    fill(255, 255, 45)
    text("Press P to pause the game.", tip4X, 465)
    tip4X = tip4X + tip4Dx
    if(tip4X > width - 250 or tip4X < 0):
        tip4Dx = -tip4Dx
        
    #start button
    
    image(start, 200, 300, 200, 100)
    
def mainPage():
    global rockY, rockX, health, score, n, rockCount, ufoMissed
    global minute, second, millisecond, currentTime, totalTime
    
    #in-game stats
    textSize(28)
    fill(255, 255, 45)
    text("Score: " + str(score), 10, 25)
    
    textSize(28)
    fill(255, 0, 0)
    text("HP: " + str(health), 275, 25)
    
    if(timeOn == True):
        currentTime = millis() - startTime + totalTime
        minute = currentTime / 1000 / 60
        second = (currentTime/1000) % 60
        millisecond = currentTime % 1000

    textSize(28)
    fill(255, 255, 45)
    text("Time: " + str(minute) + ":" + str(second) + "." + str(millisecond), 425, 25)
    
    #jet
    
    image(jet, mouseX - jetW/2, mouseY - jetH/2, jetW, jetH)
    
    #asteroids
    
    image(rock, rockX, rockY, rockW, rockH)
    rockY += rockDy
    if(rockY > height - 100):
        rockX = random(0, width - 100)
        rockY = -100
        rockCount += 1
    if(rockX + rockW > mouseX - jetW/2 + 20 and rockX < mouseX + jetW/2 - 20  and
       rockY + rockH > mouseY - jetH/2 + 20 and rockY < mouseY + jetH/2 - 20):
        health -= 1
        rockX = random(0, width - 100)
        rockY = -100    
        
    #ufos
    
    for i in range(totalNum):
        image(img[i], ufoX[i], ufoY[i], ufoW, ufoH)
        ufoY[i] = ufoY[i] + ufoDy[i]
                
        if(ufoY[i] > height):
            ufoY[i] = -random(0, height - ufoH)
            ufoX[i] = random(0, width - ufoW)
            ufoMissed += 1
    
        if(ufoX[i] + 100 > mouseX - jetW/2 + 20 and ufoX[i] < mouseX + jetW/2 - 20 and
           ufoY[i] + 100 > mouseY - jetH/2 + 20 and ufoY[i] < mouseY + jetH/2 - 20 ):
            health -= 1
            ufoX[i] = random(0, width - 100)
            ufoY[i] = -100      
        
def endPage():
    
    condition = 0
    
    # restart and exit buttons
    
    image(restart, 175, 350, 100, 100)
    image(exitGame, 325, 350, 100, 100)

    #gameover text
    
    textSize(50)
    fill(255, 0, 0)
    text("GAME OVER!", 150, 300)
    
    #final stats
    
    textSize(20)
    fill(255, 255, 70)
    text("Final score: " + str(score), 150, 500)
    
    textSize(20)
    fill(255, 255, 70)
    text("Asteroids avoided: " + str(rockCount), 150, 525)
    
    textSize(20)
    fill(255, 255, 70)
    text("UFOs missed: " + str(ufoMissed), 150, 550)
    
    textSize(20)
    fill(255, 255, 70)
    text("Time survived: " + str(minute) + ":" + str(second) + "." + str(millisecond), 150, 575)
    
def pausePage():
    
    condition = 0
    
    #paused text
    textSize(80)
    fill(255, 255, 0)
    text("PAUSED", 150, 275)
    
    #buttons
    image(resume, 125, 300, 100, 100)
    image(restart, 250, 300, 100, 100)
    image(exitGame, 375, 300, 100, 100)
    
    #in-game stats
    textSize(28)
    fill(255, 255, 45)
    text("Score: " + str(score), 10, 25)
    
    textSize(28)
    fill(255, 0, 0)
    text("HP: " + str(health), 275, 25)
    
    textSize(28)
    fill(255, 255, 45)
    text("Time: " + str(minute) + ":" + str(second) + "." + str(millisecond), 425, 25)
    
    textSize(20)
    fill(255, 255, 70)
    text("Asteroids avoided: " + str(rockCount), 150, 525)
    
    textSize(20)
    fill(255, 255, 70)
    text("UFOs missed: " + str(ufoMissed), 150, 550)
    
def mousePressed():
    global condition, bulletPosX, bulletPosY, gamePage, bulletVisible, timeOn, startTime
    
#start page

    #start button
    if(gamePage == 0):
        if(mouseX > 200 and mouseX < 400 and mouseY > 300 and mouseY < 500):
            gamePage = 1
            startTime = millis()
            timeOn = True
            
#end page

    
    if(gamePage == 2):
        
        
        #restart button
        if(mouseX > 150 and mouseX < 250 and mouseY > 350 and mouseY < 450):
            setup()
            
        #exit button
        if(mouseX > 350 and mouseX < 450 and mouseY > 350 and mouseY < 450):
            exit()
#pause page
    #resume button
    if(gamePage == 3):
        if(mouseX > 125 and mouseX < 225 and mouseY > 300 and mouseY < 400):
            gamePage = 1
            startTime = millis()
            timeOn = True
    
    #restart button
    
    if(gamePage == 3):
        if(mouseX > 250 and mouseX < 350 and mouseY > 300 and mouseY < 400):
            setup()
    
    #exit button
    
    if(gamePage == 3):
        if(mouseX > 375 and mouseX < 475 and mouseY > 300 and mouseY < 400):
            exit()

    #bullet
    if(gamePage == 1):
        bulletPosX.append(mouseX)
        bulletPosY.append(mouseY)
        bulletVisible.append(True)
        condition = 1
        if(bulletPosY < 0):
            condition = 0
            
def keyPressed():
    global gamePage, timeOn, totalTime
    
    if(gamePage == 1):
        if(key == 'p' or key == 'P'):
            gamePage = 3
            timeOn = False
            totalTime = currentTime
    
        
def drawBullet(bx, by): #bullet mechanics and scoring system 
    global bulletPosY, score
    
    for i in range(len(bulletPosY)):
        if(bulletVisible[i] == True):
            fill(0, 255, 0)
            rect(bulletPosX[i], bulletPosY[i], bulletW, bulletH)
            bulletPosY[i]-=bulletDy
            for n in range(totalNum):
                if(bulletPosY[i] < ufoY[n] + ufoH and 
                    bulletPosX[i] + bulletW > ufoX[n] and bulletPosX[i] < ufoX[n] + ufoW):
                        ufoX[n] = random(0, width - 100)
                        ufoY[n] = -100
                        score = score + 1
                        condition = 0
                        bulletVisible[i] = False
                if(bulletPosY[i] < 0):
                    bulletVisible[i] = False
                if(bulletPosY[i] < rockY + rockH and 
                    bulletPosX[i] + bulletW > rockX and bulletPosX[i] < rockX + rockH):
                    bulletVisible[i] = False
            
                
        
        
        

    

    

    


    
    
    
    
    
    
    
    
    
    
    

    

    
 
    
    
    
    
    
    
    
    
    
    
