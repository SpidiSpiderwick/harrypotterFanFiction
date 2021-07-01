from textblob import TextBlob

def getSentences(text):
    blob = TextBlob(text)
    file = open('data/hpsentences.txt', 'a')
    for sentence in blob.sentences:
        file.write(str(sentence+'\n'))

def getWordlist(text):
    blob = TextBlob(text)
    words = blob.words
    for sentence in blob.sentences:
        print(sentence.sentiment)
    print(len(words.sentiment))
    print(len(list(dict.fromkeys(blob.words))))


if __name__ == '__main__':
    text = '''
Whistle. Tick. Bzzzt. Ding. Glorp. Pop. Splat. Chime. Toot. Puff. Tinkle. Bubble. Beep. Thud. Crackle. Whoosh. Hiss. Pffft. Whirr.

Professor Flitwick had silently passed Harry a folded parchment during Charms class that Monday, and the note had said that Harry was to visit the Headmaster at his convenience and in such fashion that no one else would notice, especially not Draco Malfoy or Professor Quirrell. His one-time password for the gargoyle would be "squeamish ossifrage". This had been accompanied by a remarkably artistic ink drawing of Professor Flitwick staring at him sternly, the eyes of which occasionally blinked; and at the bottom of the note, underlined three times, was the phrase DON'T GET INTO TROUBLE.

And so Harry had finished up Transfiguration class, and studied with Hermione, and eaten dinner, and spoken with his lieutenants, and finally, when the clock struck nine, turned himself invisible and dropped back to 6PM and wearily trudged off toward the gargoyle, the turning spiral stairs, the wooden door, the room full of little fiddly things, and the silver-bearded figure of the Headmaster.

This time, Dumbledore looked quite serious, the customary smile absent; and he was dressed in pajamas of a darker and more sober purple than usual.

"Thank you for coming, Harry," said the Headmaster. The old wizard rose from his throne, began to slowly pace through the room and the strange devices. "First, do you have with you the notes of yesterday's encounter with Lucius Malfoy?"

"Notes?" blurted Harry.

"Surely you wrote it down..." said the old wizard, and his voice trailed off.

Harry felt rather embarrassed. Yes, if you'd just fumbled through a mysterious conversation full of significant hints you didn't understand, the bloody obvious thing to do would be to write it all down immediately afterward, before the memory faded, so you could try to figure it out later.

"All right," said the Headmaster, "from memory then."

Harry sheepishly recited as best he could, and got almost halfway through before he realized that it wasn't smart to just go around telling the possibly-crazy Headmaster everything, at least not without thinking about it first, but then Lucius was definitely a bad guy and Dumbledore's opponent so it probably was a good idea to tell him, and Harry had already started talking and it was too late to try and calculate things out now...

Harry finished his recollections honestly.

Dumbledore's face had grown more remote as Harry went on, and at the end there was a look of ancientness about him, a sternness in the air.

"Well," said Dumbledore. "I suggest you take the best of care that the heir of Malfoy does not come to harm, then. And I will do the same." The Headmaster was frowning, his fingers drumming soundlessly through the inky black surface of a plate inscribed with the word Leliel. "And I think it would be most extremely wise for you to avoid all interaction with Lord Malfoy henceforth."

"Did you intercept owls from him to me?" said Harry.

The Headmaster gazed at Harry for a long moment, then reluctantly nodded.

For some reason Harry wasn't feeling as outraged as he should have been. Maybe it was just that Harry was finding it very easy to sympathize with the Headmaster's point of view right now. Even Harry could understand why Dumbledore wouldn't want him to interact with Lucius Malfoy; it didn't seem like an evil deed.

Not like the Headmaster blackmailing Zabini... for which they had only Zabini's word, and Zabini was wildly untrustworthy, in fact it was hard to see why Zabini wouldn't just tell the story that got him the most sympathy from Professor Quirrell...

"How about if, instead of protesting, I say that I understand your point of view," said Harry, "and you go on intercepting my owls, but you tell me who from?"

"I have intercepted a great many owls to you, I am afraid," Dumbledore said soberly. "You are a celebrity, Harry, and you would receive dozens of letters a day, some from far outside this country, did I not turn them back."

"That," Harry said, now starting to feel a bit of indignation, "seems like going a little too far -"

"Many of those letters," the old wizard said quietly, "will be asking you for things you cannot give. I have not read them, of course, only turned them back to their senders undelivered. But I know, for I receive them too. And you are too young, Harry, to have your heart broken six times before breakfast each morning."

Harry looked down at his shoes. He should insist on reading the letters and judging for himself, but... there was a small voice of common sense inside him, and it was screaming very loudly right now.

"Thank you," Harry muttered.

"The other reason I asked you here," said the old wizard, "was that I wished to consult your unique genius."

"Transfiguration?" said Harry, surprised and flattered.

"No, not that unique genius," said Dumbledore. "Tell me, Harry, what evil could you accomplish if a Dementor were allowed onto the grounds of Hogwarts?"

It developed that Professor Quirrell had asked, or rather demanded, that his students test their skills against an actual Dementor after they learned the words and gestures to the Patronus Charm.

"Professor Quirrell is unable to cast the Patronus Charm himself," said Dumbledore, as he paced slowly through the devices. "Which is never a good sign. But then, he volunteered that fact to me in the course of demanding that outside instructors be brought in to teach the Patronus Charm to every student who wished to learn; he offered to pay the expense himself, if I would not. This impressed me greatly. But now he insists on bringing in a Dementor -"

"Headmaster," Harry said quietly, "Professor Quirrell believes very strongly in live-fire tests under realistic combat conditions. Wanting to bring in an actual Dementor is completely in character for him."

Now the Headmaster was giving Harry a strange look.

"In character? " said the old wizard.

"I mean," said Harry, "it's entirely consistent with the way Professor Quirrell usually acts..." Harry trailed off. Why had he put it that way?

The Headmaster nodded. "So you have the same sense I do; that it is an excuse. A very reasonable excuse, to be sure; more so than you may realize. Often, wizards seemingly unable to cast a Patronus Charm will succeed in the presence of an actual Dementor, going from not a single flicker of light to a full corporeal Patronus. Why this should be, no one knows; but it is so."

Harry frowned. "Then I really don't see why you're suspicious -"

The Headmaster spread his hands as though in helplessness. "Harry, the Defense Professor has asked me to pass the darkest of all creatures through the gates of Hogwarts. I must be suspicious." The Headmaster sighed. "And yet the Dementor will be guarded, warded, in a mighty cage, I will be there myself to watch it at all times - I cannot think of what ill could be done. But perhaps I am merely unable to see it. And so I am asking you."

Harry stared at the Headmaster with his mouth open. He was so shocked he couldn't even feel flattered.

"Me? " said Harry.

"Yes," said Dumbledore, smiling slightly. "I try my best to anticipate my foes, to encompass their wicked minds and predict their evil thoughts. But I would never have imagined sharpening a Hufflepuff's bones into weapons."

Was Harry ever going to live that down?

"Headmaster," Harry said wearily, "I know it doesn't sound good, but in all seriousness: I'm not evil, I'm just very creative -"

"I did not say that you were evil," Dumbledore said seriously. "There are those who say that to comprehend evil is to become evil; but they are merely pretending to be wise. Rather it is evil which does not know love, and dares not imagine love, and cannot ever understand love without ceasing to be evil. And I suspect that you can imagine your way into the minds of Dark Wizards better than I ever could, while still knowing love yourself. So, Harry." The Headmaster's eyes were intent. "If you stood in Professor Quirrell's shoes, what misdeeds could you accomplish after you tricked me into allowing a Dementor onto the grounds of Hogwarts?"

"Hold on," said Harry, and in something of a daze trudged over to the chair in front of the Headmaster's desk, and sat down. It was a large and comfortable chair this time, not a wooden stool, and Harry could feel himself enveloped as he sank into it.

Dumbledore was asking him to outwit Professor Quirrell.

Point one: Harry was rather fonder of Professor Quirrell than of Dumbledore.

Point two: The hypothesis was that the Defense Professor was planning to do something evil, and in that subjunctive case, Harry ought to be helping the Headmaster prevent it.

Point three...

"Headmaster," Harry said, "if Professor Quirrell is up to something, I'm not sure I can outwit him. He's got a lot more experience than I do."

The old wizard shook his head, somehow managing to appear very solemn despite his smile. "You underestimate yourself."

That was the first time anyone had ever said that to Harry.

"I remember," the old wizard continued, "a young man in this very office, cold and controlled as he faced down the Head of House Slytherin, blackmailing his own Headmaster to protect his classmates. And I believe that young man is more cunning than Professor Quirrell, more cunning than Lucius Malfoy, that he will grow to be the equal of Voldemort himself. It is he who I wish to consult."

Harry suppressed the chill that went through him at the name, frowned thoughtfully at the Headmaster.

How much does he know...?

The Headmaster had seen Harry in the grip of his mysterious dark side, as deep as Harry had ever sunk into it. Harry still remembered what it had been like to watch, invisibly Time-Turned, as his past self faced down the older Slytherins; the boy with the scar on his forehead who didn't act like the others. Of course the Headmaster would have noticed something odd about the boy in his office...

And Dumbledore had concluded that his pet hero had cunning to match his destined foe, the Dark Lord.

Which wasn't asking for very much, considering that the Dark Lord had put a clearly visible Dark Mark on all of his servants' left arms, and that he'd slaughtered the entire monastery that taught the martial art he'd wanted to learn.

Enough cunning to match Professor Quirrell would be a whole different order of problem.

But it was also clear that the Headmaster wouldn't be satisfied until Harry went all cold and darkish, and came up with some sort of answer that sounded impressively cunning... which had better not actually get in the way of Professor Quirrell's teaching Defense...

And of course Harry would go over to his dark side and think it through from that direction, just to be honest, and just in case.

"Tell me," Harry said, "everything about how the Dementor is to be brought in, and how it is to be guarded."

Dumbledore's eyebrows rose for a moment, and then the old wizard began to speak.

The Dementor would be transported to the grounds of Hogwarts by an Auror trio, all three personally known to the Headmaster, and all three able to cast a corporeal Patronus Charm. They would be met at the edge of the grounds by Dumbledore, who would pass the Dementor through the Hogwarts wards -

Harry asked if the pass was permanent or temporary - whether someone could just bring in the same Dementor again the next day.

The pass was temporary (replied the Headmaster with an approving nod), and the explanation went on: The Dementor would be in a cage of solid titanium bars, not Transfigured but true-forged; in time a Dementor's presence would corrode that metal to dust, but not in a single day.

Students awaiting their turn would stay well back of the Dementor, behind two corporeal Patronuses maintained by two of the three Aurors at any given time. Dumbledore would wait by the Dementor's cage with his Patronus. A single student would approach the Dementor; and Dumbledore would dispel his Patronus; and the student would attempt to cast their own Patronus Charm; and if they failed, Dumbledore would restore his Patronus before the student could suffer any permanent damage. Past dueling champion Professor Flitwick would also be present while there were students near, just to add safety margin.

"Why just you waiting by the Dementor?" said Harry. "I mean, shouldn't it be you plus an Auror -"

The Headmaster shook his head. "They could not withstand the repeated exposure to the Dementor, each time I dispel my Patronus."

And if Dumbledore's Patronus did fail for some reason, while one of the students was still near the Dementor, the third Auror would cast another corporeal Patronus and send it to shield the student...

Harry poked and prodded, but he couldn't see a flaw in the security.

So Harry took a deep breath, sank further into the chair, closed his eyes, and remembered:

"And that will be... five points? No, let us make it an even ten points from Ravenclaw for backchat."

The cold came more slowly now, more reluctantly, Harry hadn't been calling much on his dark side lately...

Harry had to run through that entire session in Potions in his mind, before his blood chilled into something approaching deadly crystalline clarity.

And then he thought of the Dementor.

And it was obvious.

"The Dementor is a distraction," Harry said. The coldness clear in his voice, since that was what Dumbledore wanted and expected. "A large, salient threat, but in the end straightforward, and easy to defend against. So while all your attention is focused on the Dementor, the real plot will be happening elsewhere."

Dumbledore stared at Harry for a moment, and then gave a slow nod. "Yes..." said the Headmaster. "And I do believe I know what it might be a distraction from, if Professor Quirrell means ill... thank you, Harry."

The Headmaster was still staring at Harry, a strange look in those ancient eyes.

"What? " said Harry with a tinge of annoyance, the cold still lingering in his blood.

"I have another question for that young man," said the Headmaster. "It is something I have long wondered to myself, yet been unable to comprehend. Why? " There was a tinge of pain in his voice. "Why would anyone deliberately make himself a monster? Why do evil for the sake of evil? Why Voldemort?"

Whirr, bzzzt, tick; ding, puff, splat...

Harry stared at the Headmaster in surprise.

"How would I know?" said Harry. "Am I supposed to magically understand the Dark Lord because I'm the hero, or something?"

"Yes! " said Dumbledore. "My own great foe was Grindelwald, and him I understood very well indeed. Grindelwald was my dark mirror, the man I could so easily have been, had I given in to the temptation to believe that I was a good person, and therefore always in the right. For the greater good, that was his slogan; and he truly believed it himself, even as he tore at all Europe like a wounded animal. And him, I defeated in the end. But then after him came Voldemort, to destroy everything I had protected in Britain." The hurt was plain now in Dumbledore's voice, exposed upon his face. "He committed acts worse by far than Grindelwald's worst, horror for the sake of horror. I sacrificed everything only to hold him back, and I still don't understand why! Why, Harry? Why did he do it? He was never my destined foe, but yours, so if you have any guesses at all, Harry, please tell me! Why? "

Harry stared down at his hands. The truth was that Harry hadn't read up on the Dark Lord yet, and right now he hadn't the tiniest clue. And somehow that didn't seem like an answer the Headmaster wanted to hear. "Too many Dark rituals, maybe? In the beginning he thought he'd do just one, but it sacrificed part of his good side, and that made him less reluctant to perform other Dark rituals, so he did more and more rituals in a positive feedback cycle until he ended up as a tremendously powerful monster -"

"No!" Now the Headmaster's voice was agonized. "I can't believe that, Harry! There has to be something more to it than just that!"

Why should there be? thought Harry, but he didn't say it, because it was clear that the Headmaster thought the universe was a story and had a plot, and that huge tragedies weren't allowed to happen except for equally huge, significant reasons. "I'm sorry, Headmaster. The Dark Lord doesn't seem like much of a dark mirror to me, not at all. There isn't anything I find even the tiniest bit tempting about nailing the skins of Yermy Wibble's family to a newsroom wall."

"Have you no wisdom to share?" said Dumbledore. There was pleading in the old wizard's voice, almost begging.

Evil happens, thought Harry, it doesn't mean anything or teach us anything, except to not be evil? The Dark Lord was probably just a selfish bastard who didn't care who he hurt, or an idiot who made stupidly avoidable mistakes that snowballed. There is no destiny behind the ills of this world; if Hitler had been allowed into architecture school like he wanted, the whole history of Europe would have been different; if we lived in the sort of universe where horrible things were only allowed to happen for good reasons, they just wouldn't happen in the first place.

And none of that, obviously, was what the Headmaster wanted to hear.

The old wizard was still looking at Harry from over a fiddly thing like a frozen puff of smoke, a painful desperation in those ancient, waiting eyes.

Well, sounding wise wasn't difficult. It was a lot easier than being intelligent, actually, since you didn't have to say anything surprising or come up with any new insights. You just let your brain's pattern-matching software complete the cliche, using whatever Deep Wisdom you'd stored previously.

"Headmaster," Harry said solemnly, "I would rather not define myself by my enemies."

Somehow, even in the midst of all the whirring and ticking, there was a kind of silence.

That had come out a bit more Deeply Wise than Harry had intended.

"You may be very wise, Harry..." the Headmaster said slowly. "I do wish... that I could have been defined by my friends." The pain in his voice had grown deeper.

Harry's mind searched hastily for something else Deeply Wise to say that would soften the unintended force of the blow -

"Or perhaps," Harry said more softly, "it is the foe that makes the Gryffindor, as it is the friend that makes the Hufflepuff, and the ambition that makes the Slytherin. I do know that it is always, in every generation, the puzzle that makes the scientist."

"It is a dreadful fate to which you condemn my House, Harry," said the Headmaster. The pain was still in his voice. "For now that you remark on it, I do think that I was very much made by my enemies."

Harry stared at his own hands, where they lay in his lap. Maybe he should just shut up while he was ahead.

"But you have answered my question," said Dumbledore more softly, as though to himself. "I should have realized that would be a Slytherin's key. For his ambition, all for the sake of his ambition; and that I know, though not why..." For a time Dumbledore stared off into nothingness; then he straightened, and his eyes seemed to focus on Harry again.

"And you, Harry," said the Headmaster, "you name yourself a scientist? " His voice was laced with surprise and mild disapproval.

"You don't like science?" said Harry a little wearily. He'd hoped Dumbledore would be fonder of Muggle things.

"I suppose it is useful to those without wands," said Dumbledore, frowning. "But it seems a strange thing by which to define yourself. Is science as important as love? As kindness? As friendship? Is it science that makes you fond of Minerva McGonagall? Is it science that makes you care for Hermione Granger? Will it be science to which you turn, when you try to kindle warmth in Draco Malfoy's heart?"

You know, the sad thing is, you probably think you just uttered some kind of incredibly wise knockdown argument.

Now, how to phrase the rejoinder in such fashion that it also sounded incredibly wise...

"You are not Ravenclaw," Harry said with calm dignity, "and so it might not have occurred to you that to respect the truth, and seek it all the days of your life, could also be an act of grace."

The Headmaster's eyebrows rose up. And then he sighed. "How did you become so wise, so young...?" The old wizard sounded sad, as he said it. "Perhaps it will prove valuable to you."

Only for impressing ancient wizards who are overly impressed with themselves, thought Harry. He was actually a bit disappointed by Dumbledore's credulity; it wasn't that Harry had lied, but Dumbledore seemed far too impressed with Harry's ability to phrase things so that they sounded profound, instead of putting them into plain English like Richard Feynman had done with his wisdom...

"Love is more important than wisdom," said Harry, just to test the limits of Dumbledore's tolerance for blindingly obvious cliches completed by sheer pattern matching without any sort of detailed analysis.

The Headmaster nodded gravely, and said, "Indeed."

Harry stood up out of the chair, and stretched his arms. Well, I'd better go off and love something, then, that's bound to help me defeat the Dark Lord. And next time you ask me for advice, I'll just give you a hug -

"This day you have helped me much, Harry," said the Headmaster. "And so there is one last thing I would ask that young man."

Great.

"Tell me, Harry," said the Headmaster (and now his voice sounded simply puzzled, though there was still a hint of pain in his eyes), "why do Dark Wizards fear death so greatly?"

"Er," said Harry, "sorry, I've got to back the Dark Wizards on that one."

Whoosh, hiss, chime; glorp, pop, bubble -

"What? " said Dumbledore.

"Death is bad," said Harry, discarding wisdom for the sake of clear communication. "Very bad. Extremely bad. Being scared of death is like being scared of a great big monster with poisonous fangs. It actually makes a great deal of sense, and does not, in fact, indicate that you have a psychological problem."

The Headmaster was staring at him as though he'd just turned into a cat.

"Okay," said Harry, "let me put it this way. Do you want to die? Because if so, there's this Muggle thing called a suicide prevention hotline -"

"When it is time," the old wizard said quietly. "Not before. I would never seek to hasten the day, nor seek to refuse it when it comes."

Harry was frowning sternly. "That doesn't sound like you have a very strong will to live, Headmaster!"

"Harry..." The old wizard's voice was starting to sound a little helpless; and he had paced to a spot where his silver beard, unnoticed, had drifted into a crystalline glass goldfish bowl, and was slowly taking on a greenish tinge that crept up the hairs. "I think I may have not made myself clear. Dark Wizards are not eager to live. They fear death. They do not reach up toward the sun's light, but flee the coming of night into infinitely darker caverns of their own making, without moon or stars. It is not life they desire, but immortality; and they are so driven to grasp at it that they will sacrifice their very souls! Do you want to live forever, Harry?"

"Yes, and so do you," said Harry. "I want to live one more day. Tomorrow I will still want to live one more day. Therefore I want to live forever, proof by induction on the positive integers. If you don't want to die, it means you want to live forever. If you don't want to live forever, it means you want to die. You've got to do one or the other... I'm not getting through here, am I."

The two cultures stared at each other across a vast gap of incommensurability.

"I have lived a hundred and ten years," the old wizard said quietly (taking his beard out of the bowl, and jiggling it to shake out the color). "I have seen and done a great many things, too many of which I wish I had never seen or done. And yet I do not regret being alive, for watching my students grow is a joy that has not begun to wear on me. But I would not wish to live so long that it does! What would you do with eternity, Harry?"

Harry took a deep breath. "Meet all the interesting people in the world, read all the good books and then write something even better, celebrate my first grandchild's tenth birthday party on the Moon, celebrate my first great-great-great grandchild's hundredth birthday party around the Rings of Saturn, learn the deepest and final rules of Nature, understand the nature of consciousness, find out why anything exists in the first place, visit other stars, discover aliens, create aliens, rendezvous with everyone for a party on the other side of the Milky Way once we've explored the whole thing, meet up with everyone else who was born on Old Earth to watch the Sun finally go out, and I used to worry about finding a way to escape this universe before it ran out of negentropy but I'm a lot more hopeful now that I've discovered the so-called laws of physics are just optional guidelines."

"I did not understand much of that," said Dumbledore. "But I must ask if these are things that you truly desire so desperately, or if you only imagine them so as to imagine not being tired, as you run and run from death."

"Life is not a finite list of things that you check off before you're allowed to die," Harry said firmly. "It's life, you just go on living it. If I'm not doing those things it'll be because I've found something better."

Dumbledore sighed. His fingers drummed on a clock; as they touched it, the numerals changed to an indecipherable script, and the hands briefly appeared in different positions. "In the unlikely event that I am permitted to tarry until a hundred and fifty," said the old wizard, "I do not think I would mind. But two hundred years would be entirely too much of a good thing."

"Yes, well," Harry said, his voice a little dry as he thought of his Mum and Dad and their allotted span if Harry didn't do something about it, "I suspect, Headmaster, that if you came from a culture where people were accustomed to living four hundred years, that dying at two hundred would seem just as tragically premature as dying at, say, eighty." Harry's voice went hard, on that last word.

"Perhaps," the old wizard said peacefully. "I would not wish to die before my friends, nor live on after they had all gone. The hardest time is when those you loved the most have gone on before you, and yet others still live, for whose sake you must stay..." Dumbledore's eyes were fixed on Harry, and growing sad. "Do not mourn me too greatly, Harry, when my time comes; I will be with those I have long missed, on our next great adventure."

"Oh!" Harry said in sudden realization. "You believe in an afterlife. I got the impression wizards didn't have religion?"

Toot. Beep. Thud.

"How can you not believe it? " said the Headmaster, looking completely flabbergasted. "Harry, you're a wizard! You've seen ghosts! "

"Ghosts," Harry said, his voice flat. "You mean those things like portraits, stored memories and behaviors with no awareness or life, accidentally impressed into the surrounding material by the burst of magic that accompanies the violent death of a wizard -"

"I've heard that theory," said the Headmaster, his voice growing sharp, "repeated by wizards who mistake cynicism for wisdom, who think that to look down upon others is to elevate themselves. It is one of the silliest ideas I have heard in a hundred and ten years! Yes, ghosts do not learn or grow, because this is not where they belong! Souls are meant to move on, there is no life remaining for them here! And if not ghosts, then what of the Veil? What of the Resurrection Stone?"

"All right," Harry said, trying to keep his voice calm, "I'll hear out your evidence, because that's what a scientist does. But first, Headmaster, let me tell you a little story." Harry's voice was trembling. "You know, when I got here, when I got off the train from King's Cross, I don't mean yesterday but back in September, when I got off the train then, Headmaster, I'd never seen a ghost. I wasn't expecting ghosts. So when I saw them, Headmaster, I did something really dumb. I jumped to conclusions. I, I thought there was an afterlife, I thought no one had ever really died, I thought that everyone the human species had ever lost was really fine after all, I thought that wizards could talk to people who'd passed on, that it just took the right spell to summon them, that wizards could do that, I thought I could meet my parents who died for me, and tell them that I'd heard about their sacrifice and that I'd begun to call them my mother and father -"

"Harry," whispered Dumbledore. Water glittered in the old wizard's eyes. He took a step closer across the office -

"And then," spat Harry, the fury coming fully into his voice, the cold rage at the universe for being like that and at himself for being so stupid, "I asked Hermione and she said that they were just afterimages, burned into the stone of the castle by the death of a wizard, like the silhouettes left on the walls of Hiroshima. And I should have known! I should have known without even having to ask! I shouldn't have believed it even for all of thirty seconds! Because if people had souls there wouldn't be any such thing as brain damage, if your soul could go on speaking after your whole brain was gone, how could damage to the left cerebral hemisphere take away your ability to talk? And Professor McGonagall, when she told me about how my parents had died, she didn't act like they'd just gone away on a long trip to another country, like they'd emigrated to Australia back in the days of sailing ships, which is the way people would act if they actually knew that death was just going somewhere else, if they had hard evidence for an afterlife, instead of making stuff up to console themselves, it would change everything, it wouldn't matter that everyone had lost someone in the war, it would be a little sad but not horrible! And I'd already seen that people in the wizarding world didn't act like that! So I should have known better! And that was when I knew that my parents were really dead and gone forever and ever, that there wasn't anything left of them, that I'd never get a chance to meet them and, and, and the other children thought I was crying because I was scared of ghosts -"

The old wizard's face was horrified, he opened his mouth to speak -

"So tell me, Headmaster! Tell me about the evidence! But don't you dare exaggerate a single tiny bit of it, because if you give me false hope again, and I find out later that you lied or stretched things just a little, I won't ever forgive you for it! What's the Veil? "

Harry reached up and wiped at his cheeks, while the glass things of the office stopped vibrating from his last shriek.

"The Veil," said the old wizard with only a slight tremble in his voice, "is a great stone archway, kept in the Department of Mysteries; a gateway to the land of the dead."

"And how does anyone know that?" said Harry. "Don't tell me what you believe, tell me what you've seen! "

The physical manifestation of the barrier between worlds was a great stone archway, old and tall and coming to a sharp point, with a tattered black veil like the surface of a pool of water, stretched between the stones; rippling, always, from the constant and one-way passage of the souls. If you stood by the Veil you could hear the voices of the dead calling, always calling in whispers barely on the wrong side of comprehension, growing louder and more numerous if you stayed and tried to hear, as they tried to communicate; and if you listened too long, you would go to meet them, and in the moment you touched the Veil you would be sucked through, and never be heard from again.

"That doesn't even sound like an interesting fraud," Harry said, his voice calmer now that there was nothing there to make him hope, or make him angry for having hopes dashed. "Someone built a stone archway, made a little black rippling surface between it that Vanished anything it touched, and enchanted it to whisper to people and hypnotize them."

"Harry..." the Headmaster said, starting to look rather worried. "I can tell you the truth, but if you refuse to hear it..."

Also not interesting. "What's the Resurrection Stone?"

"I would not tell you," the Headmaster said slowly, "save that I fear what this disbelief may do to you... so listen, then, Harry, please listen..."

The Resurrection Stone was one of the three legendary Deathly Hallows, kin to Harry's cloak. The Resurrection Stone could call souls back from the dead - bring them back into the world of the living, though not as they were. Cadmus Peverell used the stone to call back his lost beloved from the dead, but her heart stayed with the dead, and not in the world of the living. And in time it drove him mad, and he killed himself to be truly with her once more...

In all politeness, Harry raised his hand.

"Yes?" the Headmaster said reluctantly.

"The obvious test to see if the Resurrection Stone is really calling back the dead, or just projecting an image from the user's mind, is to ask a question whose answer you don't know, but the dead person would, and that can be definitely verified in this world. For example, call back -"

Then Harry paused, because this time he'd managed to think it through one step ahead of his tongue, fast enough to not say the first name and test that had sprung to mind.

"...your dead wife, and ask her where she left her lost earring, or something like that," Harry finished. "Did anyone do any tests like that?"

"The Resurrection Stone has been lost for centuries, Harry," the Headmaster said quietly.

Harry shrugged. "Well, I'm a scientist, and I'm always willing to be convinced. If you really believe the Resurrection Stone calls back the dead - then you must believe a test like that will succeed, right? So do you know anything about where to find the Resurrection Stone? I got one Deathly Hallow already under highly mysterious circumstances, and, well, we both know how the rhythm of the world works on that sort of thing."

Dumbledore stared at Harry.

Harry gazed equably back at the Headmaster.

The old wizard passed a hand across his forehead and muttered, "This is madness."

(Somehow, Harry managed to stop himself from laughing.)

And Dumbledore told Harry to draw forth the Cloak of Invisibility from his pouch; at the Headmaster's direction, Harry stared at the inside and back of the hood until he saw it, faintly drawn against the silvery mesh in faded scarlet like dried blood, the symbol of the Deathly Hallows: a triangle, with a circle drawn inside, and a line dividing them both.

"Thank you," Harry said politely. "I shall be sure to keep an eye out for a stone so marked. Do you have any other evidence?"

Dumbledore appeared to be fighting a struggle within himself. "Harry," the old wizard said, his voice rising, "this is a dangerous road you are walking, I am not sure I do the right thing by saying this, but I must wrench you from this way! Harry, how could Voldemort have survived the death of his body if he did not have a soul? "

And that was when Harry realized that there was exactly one person who'd originally told Professor McGonagall that the Dark Lord was still alive in the first place; and it was the crazy Headmaster of their madhouse of a school, who thought the world ran on cliches.

"Good question," Harry said, after some internal debate about how to proceed. "Maybe he found some way of duplicating the power of the Resurrection Stone, only he loaded it in advance with a complete copy of his brain state. Or something like that." Harry was suddenly far from sure that he was trying to come up with an explanation for something that had actually happened. "Actually, can you just go ahead and tell me everything you know about how the Dark Lord survived and what it might take to kill him?" If he even still exists as more than Quibbler headlines.

"You are not fooling me, Harry," said the old wizard; his face looked ancient now, and lined by more than years. "I know why you are truly asking that question. No, I do not read your mind, I do not have to, your hesitation gives you away! You seek the secret of the Dark Lord's immortality in order to use it for yourself!"

"Wrong! I want the secret of the Dark Lord's immortality in order to use it for everyone! "

Tick, crackle, fzzzt...

Albus Percival Wulfric Brian Dumbledore just stood there and stared at Harry with his mouth gaping open dumbly.

(Harry awarded himself a tally mark for Monday, since he'd managed to blow someone's mind completely before the day was over.)

"And in case it wasn't clear," said Harry, "by everyone I mean all Muggles too, not just all wizards."

"No," said the old wizard, shaking his head. His voice rose. "No, no, no! This is insanity! "

"Bwa ha ha!" said Harry.

The old wizard's face was tight with anger and worry. "Voldemort stole the book from which he gleaned his secret; it was not there when I went to look for it. But this much I know, and this much I will tell you: his immortality was born of a ritual terrible and Dark, blacker than pitchest black! And it was Myrtle, poor sweet Myrtle, who died for it; his immortality took sacrifice, it took murder -"

"Well obviously I'm not going to popularize a method of immortality that requires killing people! That would defeat the entire point! "

There was a startled pause.

Slowly the old wizard's face relaxed out of its anger, though the worry was still there. "You would use no ritual requiring human sacrifice."

"I don't know what you take me for, Headmaster," Harry said coldly, his own anger rising, "but let's not forget that I'm the one who wants people to live! The one who wants to save everyone! You're the one who thinks death is awesome and everyone ought to die!"

"I am at a loss, Harry," said the old wizard. His feet once more began trudging across his strange office. "I know not what to say." He picked up a crystal ball that seemed to hold a hand in flames, looked into it with a sad expression. "Only that I am greatly misunderstood by you... I don't want everyone to die, Harry!"

"You just don't want anyone to be immortal," Harry said with considerable irony. It seemed that elementary logical tautologies like All x: Die(x) = Not Exist x: Not Die(x) were beyond the reasoning abilities of the world's most powerful wizard.

The old wizard nodded. "I am less afraid than I was, but still greatly worried for you, Harry," he said quietly. His hand, a little wizened by time, but still strong, placed the crystal ball firmly back into its stand. "For the fear of death is a bitter thing, an illness of the soul by which people are twisted and warped. Voldemort is not the only Dark Wizard to go down that bleak road, though I fear he has taken it further than any before him."

"And you think you're not afraid of death?" Harry said, not even trying to mask the incredulity in his voice.

The old wizard's face was peaceful. "I am not perfect, Harry, but I think I have accepted my death as part of myself."

"Uh huh," Harry said. "See, there's this little thing called cognitive dissonance, or in plainer English, sour grapes. If people were hit on the heads with truncheons once a month, and no one could do anything about it, pretty soon there'd be all sorts of philosophers, pretending to be wise as you put it, who found all sorts of amazing benefits to being hit on the head with a truncheon once a month. Like, it makes you tougher, or it makes you happier on the days when you're not getting hit with a truncheon. But if you went up to someone who wasn't getting hit, and you asked them if they wanted to start, in exchange for those amazing benefits, they'd say no. And if you didn't have to die, if you came from somewhere that no one had ever even heard of death, and I suggested to you that it would be an amazing wonderful great idea for people to get wrinkled and old and eventually cease to exist, why, you'd have me hauled right off to a lunatic asylum! So why would anyone possibly think any thought so silly as that death is a good thing? Because you're afraid of it, because you don't really want to die, and that thought hurts so much inside you that you have to rationalize it away, do something to numb the pain, so you won't have to think about it -"

"No, Harry," the old wizard said. His face was gentle, his hand trailed through a lighted pool of water that made small musical chimes as his fingers stirred it. "Though I can understand how you must think so."

"Do you want to understand the Dark Wizard?" Harry said, his voice now hard and grim. "Then look within the part of yourself that flees not from death but from the fear of death, that finds that fear so unbearable that it will embrace Death as a friend and cozen up to it, try to become one with the night so that it can think itself master of the abyss. You have taken the most terrible of all evils and called it good! With only a slight twist that same part of yourself would murder innocents, and call it friendship. If you can call death better than life then you can twist your moral compass to point anywhere -"

"I think," said Dumbledore, shaking water droplets from his hand to the sound of tiny tinkling bells, "that you understand Dark Wizards very well, without yet being one yourself." It was said in perfect seriousness, and without accusation. "But your comprehension of me, I fear, is sorely lacking." The old wizard was smiling now, and there was a gentle laughter in his voice.

Harry was trying not to go any colder than he already was; from somewhere there was pouring into his mind a blazing fury of resentment, at Dumbledore's condescension, and all the laughter that wise old fools had ever used in place of argument. "Funny thing, you know, I thought Draco Malfoy was going to be this impossible to talk to, and instead, in his childish innocence, he was a hundred times stronger than you."

A look of puzzlement crossed the old wizard's face. "What do you mean?"

"I mean," Harry said, his voice biting, "that Draco actually took his own beliefs seriously and processed my words instead of throwing them out the window by smiling with gentle superiority. You're so old and wise, you can't even notice anything I'm saying! Not understand, notice! "

"I have listened to you, Harry," said Dumbledore, looking more solemn now, "but to listen is not always to agree. Disagreements aside, what is it that you think I do not comprehend?"

That if you really believed in an afterlife, you'd go down to St. Mungo's and kill Neville's parents, Alice and Frank Longbottom, so they could go on to their next great adventure, instead of letting them linger here in their damaged state -

Harry barely, barely kept himself from saying it out loud.

"All right," Harry said coldly. "I'll answer your original question, then. You asked why Dark Wizards are afraid of death. Pretend, Headmaster, that you really believed in souls. Pretend that anyone could verify the existence of souls at any time, pretend that nobody cried at funerals because they knew their loved ones were still alive. Now can you imagine destroying a soul? Ripping it to shreds so that nothing remains to go on its next great adventure? Can you imagine what a terrible thing that would be, the worst crime that had ever been committed in the history of the universe, which you would do anything to prevent from happening even once? Because that's what Death really is - the annihilation of a soul!"

The old wizard was staring at him, a sad look in his eyes. "I suppose I do understand now," he said quietly.

"Oh?" said Harry. "Understand what?"

"Voldemort," said the old wizard. "I understand him now at last. Because to believe that the world is truly like that, you must believe there is no justice in it, that it is woven of darkness at its core. I asked you why he became a monster, and you could give no reason. And if I could ask him, I suppose, his answer would be: Why not?"

They stood there gazing into each other's eyes, the old wizard in his robes, and the young boy with the lightning-bolt scar on his forehead.

"Tell me, Harry," said the old wizard, "will you become a monster?"

"No," said the boy, an iron certainty in his voice.

"Why not?" said the old wizard.

The young boy stood very straight, his chin raised high and proud, and said: "There is no justice in the laws of Nature, Headmaster, no term for fairness in the equations of motion. The universe is neither evil, nor good, it simply does not care. The stars don't care, or the Sun, or the sky. But they don't have to! We care! There is light in the world, and it is us! "

"I wonder what will become of you, Harry," said the old wizard. His voice was soft, with a strange wonder and regret in it. "It is enough to make me wish to live just to see it."

The boy bowed to him with heavy irony, and departed; and the oaken door slammed shut behind him with a thud.

    '''
    #getSentences(text)
    getWordlist(text)

