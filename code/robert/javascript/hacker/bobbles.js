let terminal_log = document.querySelector('#terminal')
const story = `
=== Nuka-World ===            

System Access

================================
= Fun House =
= Room Control Systems =
================================

Hall of Mirrors

...................................................

::: SYSTEM ERROR :::

Communication could not be established.

Bottle Jumps

...................................................

::: SYSTEM ERROR :::

Communication could not be established.

Hypno Halls

================================
= Fun House =
= Halls of Hallucination =
================================

Set Reduced Nausea Mode On

:::System Message:::

System Set to Reduced Nausea Mode.

Set Reduced Nausea Mode Off

:::System Message:::

System Set to Normal Mode.

Spinning Room

================================
= Fun House =
= Spinning Room =
================================

Turn Spinning Floor Off

:::System Message:::

Spinning Floor Set to Off.

Set Reduced Nausea Mode On

:::System Message:::

Spinning Floor Set to On.

User Logs

================================
= User Logs =
= < Herman Benson Signed In> =
================================

Living in the fun house

After the crew divided up the park for living accommidations

In-game spelling, Bradley is over the moon. We get to live in the Fun House! 

It's a ton of room, but every memory I have of this place involves someone getting nauseous from the spinning.

I'm glad he's happy about it at least, it's been far too long since I saw a smile like that on his face. 

I don't think he's realized it yet with everything that's been going on, 

but he would have graduated high school last month. 

I know it's selfish, but part of me is glad that the attack happened when it did so I can have my son here, 

safe with me.

Out in the storm

Woke up to find that Bradley had gone out in a radiation storm. 

He said he couldn't take living like this and if the radiation was going to kill us, 

he'd rather die quickly. 

I don't know if he'll ever realize how much it hurt me to hear him say that.

Luckily the storm doesn't seem to have hurt him at all. 

In fact, 

that ankle he sprained messing around in the spinning room last week seems to have instantly healed. 

Maybe whatever mutation the initial storms gave us has somehow made us immune to radiation. 

Thank goodness for that.

Snapped during the attack

Something snapped in me during the last attack on Kiddie Kingdom. 

Maybe it was pent up rage from Bradley leaving, 

but during the attack I lost it and bit into the neck of one of the attackers.

At least, that's what they tell me. I don't remember, 

it's all hazy after the attack started. God and I'm so hungry suddenly. 

I've probably eaten twenty potatoes today, but I can't seem to shake it. 

Damn it, why am I so hungry?! Want 978097jfkjnnu90vb109

This new group is different

I haven't been in here in years. 

Not since Herman changed. This terminal is still signed in under his name. 

I can't even remember how long it's been since he was able to have a conversation. 

Maybe Rachel is right about needing to leave to find a cure for the Affliction.

Anyway, 

that new group of psychos that moved into Nuka-Town U.S.A. is clearly different than the last one.

Stronger and way more aggressive. 

They pushed us all the way back to the Fun House, which I haven't had to go into for years. 

I better start getting this place ready as a fall back again, 

it doesn't seem like those gangs are going to be dissuaded easily. 

I just hope that our defenses can hold them off long enough to find a cure.`

keypress = 0
document.addEventListener('keypress', function() {
    let storyTeller = ''
    for (let i=0;i < keypress; i++){
        storyTeller += story[i]
    }
    console.log(keypress)
    if (keypress<1000){
        keypress+=5
        terminal_log.innerHTML = `${storyTeller}`
        }
    else if (keypress<4000){
        keypress+=100
        terminal_log.innerHTML = `${storyTeller}`
    }
    else  {
        terminal_log.innerHTML = `System Error. Nuclear Activity Detected`
    }
})

