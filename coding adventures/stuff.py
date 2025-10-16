import pygame
pygame.init()
pygame.mixer.init()
import random


sip_sound = pygame.mixer.Sound("sound/sip.wav")
boba_sound = pygame.mixer.Sound("sound/ping.wav")
freeze_sound = pygame.mixer.Sound("sound/freeze.wav")

sips = 5

while sips > 0:
    print("You take a sip... 🧋")
    sip_sound.play()
    sips -= 1
    
    event = random.choice(["none", "boba_pearl", "brain_freeze", "none", "none"])
    if event == "boba_pearl":
        print("You chew on a boba pearl! Yum!")
        boba_sound.play()
    elif event == "brain_freeze":
        print("🥶 Uh oh! Brain freeze warning! Slow down!")
        freeze_sound.play()
print("Cup empty. Refill time!")