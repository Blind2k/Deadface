## Description

Players will be given a an image. The image will help detect the location.

Points: **40**
Created by: @blind2k
Dependency: N/A
Attempts: N/A

## Challenge

> Marveal is keeping his shananigens Doxing people around the world. Now we need to find the location of a person that Mirvael compromised his phone.
>
> Enter the answer as `deadface{Country_City_Street}`.

## Hints

1. The puppets are there for a reason.
2. Check the stickers in the bottom. Which languages use umlaut (ä).
3. The window can hint the street name.

## Solution

The black items in the bottom of the window contain umlaut (ä). Those are common in languages such as German/Austria/Swiss German.

![image.png](https://trello.com/1/cards/68f7376520b65c13ca7a4668/attachments/68f7394a4c304732c42d3e62/download/image.png)

Additionally, a part of the street is shown in the window reflection.

![image.png](https://trello.com/1/cards/68f7376520b65c13ca7a4668/attachments/68f7397d0253a37edb4fef46/download/image.png)

Using Google Dorks Wildcard (*) will help fill up the entire street name.

![image.png](https://trello.com/1/cards/68f7376520b65c13ca7a4668/attachments/68f739f524c8e4e946a7cebc/download/image.png)

The city where the image was taken is “Rotweill”. Combining the dogs' bread in the search query will reveal there is a town in Germany called Rottweil.

‌

![image.png](https://trello.com/1/cards/68f7376520b65c13ca7a4668/attachments/68f73a79a5fb4b82f6a52a89/download/image.png)

Eventually, put what we got so far and the location will reveal.

![image.png](https://trello.com/1/cards/68f7376520b65c13ca7a4668/attachments/68f73ab3ffae742cd18ce815/download/image.png)

## Flag

deadface{Germany\_Rottweil\_Oberamteigasse}