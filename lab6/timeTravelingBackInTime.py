"""
PosENQ - UFSC
Introduction to python to research - ENQ410034
Alison Likoski Neves - 202405086
Lab 6: matplotlib 
"""
####################################################################################################################
"""
Problem 1 - Time traveling back in time
Look within your work and find a graph you didn't like much from a previous report or your current research work, 
and make it fun and vibrant using personalized markers and colors.
####################################################################################################################
Work choosen: Data from my master's thesis, which is about the height of a water droplet while being absorbed
by a porous material (fabric) in function of time.
The data was obtained from an experiment where a water droplet was placed on a piece of fabric and the height of the 
droplet was measured at regular intervals. 
"""
####################################################################################################################
# Libs
import pandas as pd
import matplotlib.pyplot as plt

####################################################################################################################
# Constants

# Time
time = [
    0, 0.016281, 0.033342, 0.050352, 0.066512, 0.083519, 0.09965, 0.116373, 0.133318,
    0.149783, 0.166309, 0.183499, 0.199903, 0.216333, 0.232979, 0.24968, 0.266953,
    0.284012, 0.299666, 0.316236, 0.33298, 0.349876, 0.366609, 0.383386, 0.399577,
    0.416175, 0.433394, 0.449719, 0.46665, 0.482956, 0.500009, 0.516563, 0.533242,
    0.549639, 0.566182, 0.583594, 0.599715, 0.61625, 0.632902, 0.650002, 0.666612,
    0.683161, 0.699713, 0.716278, 0.733463, 0.749936, 0.766452, 0.782859, 0.799816
]
df = pd.DataFrame({'time': time})

# Height
height1 = [
    None, None, None, None, 1.43057565, 1.417269359, None, 1.671736258, None, None,
    1.460994125, None, 1.59536141, 1.578464908, None, 1.474167651, 1.444957159, 1.454971217,
    1.49398435, 1.457793294, 1.439365354, 1.422747773, 1.369555562, 1.337369121, 1.32438819,
    1.296655566, 1.223833115, 1.135646994, 0.9648998513, 1.03809824, 0.9500411241, 0.7610730655,
    0.8181326544, 0.7471446372, 0.7073338153, 0.6135141084, 0.5771750284, 0.5109803842,
    0.4407902423, 0.4373881964, 0.4078945121, 0.3484372589, 0.3188152301, 0.2919532269,
    0.2984162846, 0.2664170451, 0.2512277153, 0.2152546514, 0.1863117066
]

height2 =  [
    None, None, 2.770279344, None, 2.338845319, None, None, 2.581223583, None, 2.328335798,
    2.323746625, None, 2.421857161, 2.348212609, 2.229479736, 2.172337142, 2.120706787,
    2.137998192, 2.083573514, 2.011629074, 1.944827117, 1.87741329, 1.815209771, 1.740305374,
    1.658677398, 1.574942964, 1.494935171, 1.407945215, 1.344270034, 1.282155004, 1.216858606,
    1.143125082, 1.06552748, 1.004553786, 0.9019534473, 0.8525693708, 0.8026613688, 0.7435336346,
    0.6846999844, 0.6324250232, 0.5732049584, 0.5222722715, 0.4712122182, 0.419240322,
    0.3721316508, 0.335823136, 0.2932155202, 0.2396275099, 0.1773290844
]

df['height1'] = height1
df['height2'] = height2

####################################################################################################################
# Functions
def draw(): # Just a function to make the terminal prettier =) (and faster to print LOL)
    print()
    print("___" * 30)
    print()
####################################################################################################################
draw()
print("Lab - Time traveling back in time")
print("By: Alison Likoski Neves")
draw()
print("Old graph:")
plt.figure(figsize=(10, 5))
plt.plot(df['time'], df['height1'], label='Height 1')
plt.plot(df['time'], df['height2'], label='Height 2')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Height of water droplet in function of time')
plt.legend()
plt.show()
draw()





