﻿# TODO: Translation updated at 2025-01-26 12:26

# game/tutorial_atl.rpy:208
translate italian tutorial_positions_a09a3fd1:

    # e "In this tutorial, I'll teach you how Ren'Py positions things on the screen. But before that, let's learn a little bit about how Python handles numbers."
    e ""

# game/tutorial_atl.rpy:210
translate italian tutorial_positions_ba39aabc:

    # e "There are two main kinds of numbers in Python: integers and floating point numbers. An integer consists entirely of digits, while a floating point number has a decimal point."
    e ""

# game/tutorial_atl.rpy:212
translate italian tutorial_positions_a60b775d:

    # e "For example, 100 is an integer, while 0.5 is a floating point number, or float for short. In this system, there are two zeros: 0 is an integer, and 0.0 is a float."
    e ""

# game/tutorial_atl.rpy:214
translate italian tutorial_positions_7f1a560c:

    # e "Ren'Py uses integers to represent absolute coordinates, and floats to represent fractions of an area with known size."
    e ""

# game/tutorial_atl.rpy:216
translate italian tutorial_positions_8e7d3e52:

    # e "When we're positioning something, the area is usually the entire screen."
    e ""

# game/tutorial_atl.rpy:218
translate italian tutorial_positions_fdcf9d8b:

    # e "Let me get out of the way, and I'll show you where some positions are."
    e ""

# game/tutorial_atl.rpy:232
translate italian tutorial_positions_76d7a5bf:

    # e "The origin is the upper-left corner of the screen. That's where the x position (xpos) and the y position (ypos) are both zero."
    e ""

# game/tutorial_atl.rpy:238
translate italian tutorial_positions_be14c7c3:

    # e "When we increase xpos, we move to the right. So here's an xpos of .5, meaning half the width across the screen."
    e ""

# game/tutorial_atl.rpy:243
translate italian tutorial_positions_9b91be6c:

    # e "Increasing xpos to 1.0 moves us to the right-hand border of the screen."
    e ""

# game/tutorial_atl.rpy:249
translate italian tutorial_positions_2b293304:

    # e "We can also use an absolute xpos, which is given in an absolute number of pixels from the left side of the screen. For example, since this window is 1280 pixels across, using an xpos of 640 will return the target to the center of the top row."
    e ""

# game/tutorial_atl.rpy:251
translate italian tutorial_positions_c4d18c0a:

    # e "The y-axis position, or ypos works the same way. Right now, we have a ypos of 0.0."
    e ""

# game/tutorial_atl.rpy:257
translate italian tutorial_positions_16933a61:

    # e "Here's a ypos of 0.5."
    e ""

# game/tutorial_atl.rpy:262
translate italian tutorial_positions_6eb36777:

    # e "A ypos of 1.0 specifies a position at the bottom of the screen. If you look carefully, you can see the position indicator spinning below the text window."
    e ""

# game/tutorial_atl.rpy:264
translate italian tutorial_positions_a423050f:

    # e "Like xpos, ypos can also be an integer. In this case, ypos would give the total number of pixels from the top of the screen."
    e ""

# game/tutorial_atl.rpy:272
translate italian tutorial_positions_bc7a809a:

    # e "Can you guess where this position is, relative to the screen?" nointeract
    e "" nointeract

# game/tutorial_atl.rpy:276
translate italian tutorial_positions_6f926e18:

    # e "Sorry, that's wrong. The xpos is .75, and the ypos is .25."
    e ""

# game/tutorial_atl.rpy:278
translate italian tutorial_positions_5d5feb98:

    # e "In other words, it's 75%% of the way from the left side, and 25%% of the way from the top."
    e ""

# game/tutorial_atl.rpy:282
translate italian tutorial_positions_77b45218:

    # e "Good job! You got that position right."
    e ""

# game/tutorial_atl.rpy:286
translate italian tutorial_positions_6f926e18_1:

    # e "Sorry, that's wrong. The xpos is .75, and the ypos is .25."
    e ""

# game/tutorial_atl.rpy:288
translate italian tutorial_positions_5d5feb98_1:

    # e "In other words, it's 75%% of the way from the left side, and 25%% of the way from the top."
    e ""

# game/tutorial_atl.rpy:302
translate italian tutorial_positions_e4380a83:

    # e "The second position we care about is the anchor. The anchor is a spot on the thing being positioned."
    e ""

# game/tutorial_atl.rpy:304
translate italian tutorial_positions_d1db1246:

    # e "For example, here we have an xanchor of 0.0 and a yanchor of 0.0. It's in the upper-left corner of the logo image."
    e ""

# game/tutorial_atl.rpy:309
translate italian tutorial_positions_6056873f:

    # e "When we increase the xanchor to 1.0, the anchor moves to the right corner of the image."
    e ""

# game/tutorial_atl.rpy:314
translate italian tutorial_positions_7cdb8dcc:

    # e "Similarly, when both xanchor and yanchor are 1.0, the anchor is the bottom-right corner."
    e ""

# game/tutorial_atl.rpy:321
translate italian tutorial_positions_03a07da8:

    # e "To place an image on the screen, we need both the position and the anchor."
    e ""

# game/tutorial_atl.rpy:329
translate italian tutorial_positions_8945054f:

    # e "We then line them up, so that both the position and anchor are at the same point on the screen."
    e ""

# game/tutorial_atl.rpy:339
translate italian tutorial_positions_2b184a93:

    # e "When we place both in the upper-left corner, the image moves to the upper-left corner of the screen."
    e ""

# game/tutorial_atl.rpy:348
translate italian tutorial_positions_5aac4f3f:

    # e "With the right combination of position and anchor, any place on the screen can be specified, without even knowing the size of the image."
    e ""

# game/tutorial_atl.rpy:360
translate italian tutorial_positions_3b59b797:

    # e "It's often useful to set xpos and xanchor to the same value. We call that xalign, and it gives a fractional position on the screen."
    e ""

# game/tutorial_atl.rpy:365
translate italian tutorial_positions_b8ebf9fe:

    # e "For example, when we set xalign to 0.0, things are aligned to the left side of the screen."
    e ""

# game/tutorial_atl.rpy:370
translate italian tutorial_positions_8ce35d52:

    # e "When we set it to 1.0, then we're aligned to the right side of the screen."
    e ""

# game/tutorial_atl.rpy:375
translate italian tutorial_positions_6745825f:

    # e "And when we set it to 0.5, we're back to the center of the screen."
    e ""

# game/tutorial_atl.rpy:377
translate italian tutorial_positions_64428a07:

    # e "Setting yalign is similar, except along the y-axis."
    e ""

# game/tutorial_atl.rpy:379
translate italian tutorial_positions_cfb77d42:

    # e "Remember that xalign is just setting xpos and xanchor to the same value, and yalign is just setting ypos and yanchor to the same value."
    e ""

# game/tutorial_atl.rpy:384
translate italian tutorial_positions_cfc1723e:

    # e "The xcenter and ycenter properties position the center of the image. Here, with xcenter set to .75, the center of the image is three-quarters of the way to the right side of the screen."
    e ""

# game/tutorial_atl.rpy:389
translate italian tutorial_positions_7728dbf9:

    # e "The difference between xalign and xcenter is more obvious when xcenter is 1.0, and the image is halfway off the right side of the screen."
    e ""

# game/tutorial_atl.rpy:397
translate italian tutorial_positions_1b1cedc6:

    # e "There are the xoffset and yoffset properties, which are applied after everything else, and offset things to the right or bottom, respectively."
    e ""

# game/tutorial_atl.rpy:402
translate italian tutorial_positions_e6da2798:

    # e "Of course, you can use negative numbers to offset things to the left and top."
    e ""

# game/tutorial_atl.rpy:407
translate italian tutorial_positions_e0fe2d81:

    # e "Lastly, I'll mention that there are combined properties like align, pos, anchor, and center. Align takes a pair of numbers, and sets xalign to the first and yalign to the second. The others are similar."
    e ""

# game/tutorial_atl.rpy:414
translate italian tutorial_positions_0f4ca2b6:

    # e "Once you understand positions, you can use transformations to move things around the Ren'Py screen."
    e ""

# game/tutorial_atl.rpy:421
translate italian tutorial_atl_d5d6b62a:

    # e "Ren'Py uses transforms to animate, manipulate, and place images. We've already seen the very simplest of transforms in use:"
    e ""

# game/tutorial_atl.rpy:428
translate italian tutorial_atl_7e853c9d:

    # e "Transforms can be very simple affairs that place the image somewhere on the screen, like the right transform."
    e ""

# game/tutorial_atl.rpy:432
translate italian tutorial_atl_87a6ecbd:

    # e "But transforms can also be far more complicated affairs, that introduce animation and effects into the mix. To demonstrate, let's have a Gratuitous Rock Concert!"
    e ""

# game/tutorial_atl.rpy:440
translate italian tutorial_atl_65badef3:

    # e "But first, let's have... a Gratuitous Rock Concert!"
    e ""

# game/tutorial_atl.rpy:448
translate italian tutorial_atl_e0d3c5ec:

    # e "That was a lot of work, but it was built out of small parts."
    e ""

# game/tutorial_atl.rpy:450
translate italian tutorial_atl_f2407514:

    # e "Most transforms in Ren'Py are built using the Animation and Transform Language, or ATL for short."
    e ""

# game/tutorial_atl.rpy:452
translate italian tutorial_atl_1f22f875:

    # e "There are currently three places where ATL can be used in Ren'Py."
    e ""

# game/tutorial_atl.rpy:457
translate italian tutorial_atl_fd036bdf:

    # e "The first place ATL can be used is as part of an image statement. Instead of a displayable, an image may be defined as a block of ATL code."
    e ""

# game/tutorial_atl.rpy:459
translate italian tutorial_atl_7cad2ab9:

    # e "When used in this way, we have to be sure that ATL includes one or more displayables to actually show."
    e ""

# game/tutorial_atl.rpy:464
translate italian tutorial_atl_c78b2a1e:

    # e "The second way is through the use of the transform statement. This assigns the ATL block to a python variable, allowing it to be used in at clauses and inside other transforms."
    e ""

# game/tutorial_atl.rpy:476
translate italian tutorial_atl_da7a7759:

    # e "Finally, an ATL block can be used as part of a show statement, instead of the at clause." id tutorial_atl_da7a7759
    e "" id tutorial_atl_da7a7759

# game/tutorial_atl.rpy:483
translate italian tutorial_atl_1dd345c6:

    # e "When ATL is used as part of a show statement, values of properties exist even when the transform is changed. So even though your click stopped the motion, the image remains in the same place." id tutorial_atl_1dd345c6
    e "" id tutorial_atl_1dd345c6

# game/tutorial_atl.rpy:491
translate italian tutorial_atl_98047789:

    # e "The key to ATL is what we call composability. ATL is made up of relatively simple commands, which can be combined together to create complicated transforms."
    e ""

# game/tutorial_atl.rpy:493
translate italian tutorial_atl_ed82983f:

    # e "Before I explain how ATL works, let me explain what animation and transformation are."
    e ""

# game/tutorial_atl.rpy:498
translate italian tutorial_atl_2807adff:

    # e "Animation is when the displayable being shown changes. For example, right now I am changing my expression."
    e ""

# game/tutorial_atl.rpy:525
translate italian tutorial_atl_3eec202b:

    # e "Transformation involves moving or distorting an image. This includes placing it on the screen, zooming it in and out, rotating it, and changing its opacity."
    e ""

# game/tutorial_atl.rpy:533
translate italian tutorial_atl_fbc9bf83:

    # e "To introduce ATL, let's start by looking at a simple animation. Here's one that consists of five lines of ATL code, contained within an image statement." id tutorial_atl_fbc9bf83
    e "" id tutorial_atl_fbc9bf83

# game/tutorial_atl.rpy:535
translate italian tutorial_atl_bf92d973:

    # e "To change a displayable, simply mention it on a line of ATL. Here, we're switching back and forth between two images."
    e ""

# game/tutorial_atl.rpy:537
translate italian tutorial_atl_51a41db4:

    # e "Since we're defining an image, the first line of ATL must give a displayable. Otherwise, there would be nothing to show."
    e ""

# game/tutorial_atl.rpy:539
translate italian tutorial_atl_3d065074:

    # e "The second and fourth lines are pause statements, which cause ATL to wait half a second each before continuing. That's how we give the delay between images."
    e ""

# game/tutorial_atl.rpy:541
translate italian tutorial_atl_60f2a5e8:

    # e "The final line is a repeat statement. This causes the current block of ATL to be restarted. You can only have one repeat statement per block."
    e ""

# game/tutorial_atl.rpy:546
translate italian tutorial_atl_146cf4c4:

    # e "If we were to write repeat 2 instead, the animation would loop twice, then stop."
    e ""

# game/tutorial_atl.rpy:551
translate italian tutorial_atl_d90b1838:

    # e "Omitting the repeat statement means that the animation stops once we reach the end of the block of ATL code."
    e ""

# game/tutorial_atl.rpy:556
translate italian tutorial_atl_e5872360:

    # e "By default, displayables are replaced instantaneously. We can also use a with clause to give a transition between displayables."
    e ""

# game/tutorial_atl.rpy:563
translate italian tutorial_atl_2e9d63ea:

    # e "With animation done, we'll see how we can use ATL to transform images, starting with positioning an image on the screen."
    e ""

# game/tutorial_atl.rpy:572
translate italian tutorial_atl_ddc55039:

    # e "The simplest thing we can do is to statically position an image. This is done by giving the names of the position properties, followed by the property values." id tutorial_atl_ddc55039
    e "" id tutorial_atl_ddc55039

# game/tutorial_atl.rpy:577
translate italian tutorial_atl_43516492:

    # e "With a few more statements, we can move things around on the screen."
    e ""

# game/tutorial_atl.rpy:579
translate italian tutorial_atl_fb979287:

    # e "This example starts the image off at the top-right of the screen, and waits a second. It then moves it to the left side, waits another second, and repeats."
    e ""

# game/tutorial_atl.rpy:581
translate italian tutorial_atl_7650ec09:

    # e "The pause and repeat statements are the same statements we used in our animations. They work throughout ATL code."
    e ""

# game/tutorial_atl.rpy:586
translate italian tutorial_atl_d3416d4f:

    # e "Having the image jump around on the screen isn't all that useful. That's why ATL has the interpolation statement."
    e ""

# game/tutorial_atl.rpy:588
translate italian tutorial_atl_4e7512ec:

    # e "The interpolation statement allows you to smoothly vary the value of a transform property, from an old to a new value."
    e ""

# game/tutorial_atl.rpy:590
translate italian tutorial_atl_685eeeaa:

    # e "Here, we have an interpolation statement on the second ATL line. It starts off with the name of a time function, in this case linear."
    e ""

# game/tutorial_atl.rpy:592
translate italian tutorial_atl_c5cb49de:

    # e "That's followed by an amount of time, in this case three seconds. It ends with a list of properties, each followed by its new value."
    e ""

# game/tutorial_atl.rpy:594
translate italian tutorial_atl_04b8bc1d:

    # e "The value of each property is interpolated from its value when the statement starts to the value at the end of the statement. This is done once per frame, allowing smooth animation."
    e ""

# game/tutorial_atl.rpy:605
translate italian tutorial_atl_2958f397:

    # e "ATL supports more complicated move types, like circle and spline motion. But I won't be showing those here."
    e ""

# game/tutorial_atl.rpy:609
translate italian tutorial_atl_d08fe8d9:

    # e "Apart from displayables, pause, interpolation, and repeat, there are a few other statements we can use as part of ATL."
    e ""

# game/tutorial_atl.rpy:621
translate italian tutorial_atl_84b22ac0:

    # e "ATL transforms created using the statement become ATL statements themselves. Since the default positions are also transforms, this means that we can use left, right, and center inside of an ATL block."
    e ""

# game/tutorial_atl.rpy:637
translate italian tutorial_atl_331126c1:

    # e "Here, we have two new statements. The block statement allows you to include a block of ATL code. Since the repeat statement applies to blocks, this lets you repeat only part of an ATL transform."
    e ""

# game/tutorial_atl.rpy:639
translate italian tutorial_atl_24f67b67:

    # e "We also have the time statement, which runs after the given number of seconds have elapsed from the start of the block. It will run even if another statement is running, stopping the other statement."
    e ""

# game/tutorial_atl.rpy:641
translate italian tutorial_atl_b7709507:

    # e "So this example bounces the image back and forth for eleven and a half seconds, and then moves it to the right side of the screen."
    e ""

# game/tutorial_atl.rpy:655
translate italian tutorial_atl_f903bc3b:

    # e "The parallel statement lets us run two blocks of ATL code at the same time."
    e ""

# game/tutorial_atl.rpy:657
translate italian tutorial_atl_5d0f8f9d:

    # e "Here, the top block move the image in the horizontal direction, and the bottom block moves it in the vertical direction. Since they're moving at different speeds, it looks like the image is bouncing on the screen."
    e ""

# game/tutorial_atl.rpy:671
translate italian tutorial_atl_28a7d27e:

    # e "Finally, the choice statement makes Ren'Py randomly pick a block of ATL code. This allows you to add some variation as to what Ren'Py shows."
    e ""

# game/tutorial_atl.rpy:677
translate italian tutorial_atl_2265254b:

    # e "This tutorial game has only scratched the surface of what you can do with ATL. For example, we haven't even covered the on and event statements. For more information, you might want to check out {a=https://renpy.org/doc/html/atl.html}the ATL chapter in the reference manual{/a}."
    e ""

# game/tutorial_atl.rpy:686
translate italian transform_properties_391169cf:

    # e "Ren'Py has quite a few transform properties that can be used with ATL, the Transform displayable, and the add Screen Language statement."
    e ""

# game/tutorial_atl.rpy:687
translate italian transform_properties_fc895a1f:

    # e "Here, we'll show them off so you can see them in action and get used to what each does."
    e ""

# game/tutorial_atl.rpy:703
translate italian transform_properties_88daf990:

    # e "First off, all of the position properties are also transform properties. These include the pos, anchor, align, center, and offset properties."
    e ""

# game/tutorial_atl.rpy:721
translate italian transform_properties_d7a487f1:

    # e "The position properties can also be used to pan over a displayable larger than the screen, by giving xpos and ypos negative values."
    e ""

# game/tutorial_atl.rpy:731
translate italian transform_properties_89e0d7c2:

    # "The subpixel property controls how things are lined up with the screen. When False, images can be pixel-perfect, but there can be pixel jumping."
    ""

# game/tutorial_atl.rpy:738
translate italian transform_properties_4194527e:

    # "When it's set to True, movement is smoother at the cost of blurring images a little."
    ""

# game/tutorial_atl.rpy:757
translate italian transform_properties_35934e77:

    # e "Transforms also support polar coordinates. The around property sets the center of the coordinate system to coordinates given in pixels."
    e ""

# game/tutorial_atl.rpy:765
translate italian transform_properties_605ebd0c:

    # e "The angle property gives the angle in degrees. Angles run clockwise, with the zero angle at the top of the screen."
    e ""

# game/tutorial_atl.rpy:774
translate italian transform_properties_6d4555ed:

    # e "The radius property gives the distance in pixels from the anchor of the displayable to the center of the coordinate system."
    e ""

# game/tutorial_atl.rpy:788
translate italian transform_properties_7af037a5:

    # e "There are several ways to resize a displayable. The zoom property lets us scale a displayable by a factor, making it bigger and smaller."
    e ""

# game/tutorial_atl.rpy:801
translate italian transform_properties_b6527546:

    # e "The xzoom and yzoom properties allow the displayable to be scaled in the X and Y directions independently."
    e ""

# game/tutorial_atl.rpy:811
translate italian transform_properties_b98b780b:

    # e "By making xzoom or yzoom a negative number, we can flip the image horizontally or vertically."
    e ""

# game/tutorial_atl.rpy:821
translate italian transform_properties_74d542ff:

    # e "Instead of zooming by a scale factor, the size transform property can be used to scale a displayable to a size in pixels."
    e ""

# game/tutorial_atl.rpy:836
translate italian transform_properties_438ed776:

    # e "The alpha property is used to change the opacity of a displayable. This can make it appear and disappear."
    e ""

# game/tutorial_atl.rpy:849
translate italian transform_properties_aee19f86:

    # e "The rotate property rotates a displayable."
    e ""

# game/tutorial_atl.rpy:860
translate italian transform_properties_57b3235a:

    # e "By default, when a displayable is rotated, Ren'Py will include extra space on all four sides, so the size doesn't change as it rotates. Here, you can see the extra space on the left and top, and it's also there on the right and bottom."
    e ""

# game/tutorial_atl.rpy:872
translate italian transform_properties_66d29ee8:

    # e "By setting rotate_pad to False, we can get rid of the space, at the cost of the size of the displayable changing as it rotates."
    e ""

# game/tutorial_atl.rpy:883
translate italian transform_properties_7f32e8ad:

    # e "The tile transform properties, xtile and ytile, repeat the displayable multiple times."
    e ""

# game/tutorial_atl.rpy:893
translate italian transform_properties_207b7fc8:

    # e "The crop property crops a rectangle out of a displayable, showing only part of it."
    e ""

# game/tutorial_atl.rpy:907
translate italian transform_properties_e7e22d28:

    # e "When used together, crop and size can be used to focus in on specific parts of an image."
    e ""

# game/tutorial_atl.rpy:919
translate italian transform_properties_f34abd82:

    # e "The xpan and ypan properties can be used to pan over a displayable, given an angle in degrees, with 0 being the center."
    e ""

# game/tutorial_atl.rpy:926
translate italian transform_properties_bfa3b139:

    # e "Those are all the transform properties we have to work with. By putting them together in the right order, you can create complex things."
    e ""

translate italian strings:

    # game/tutorial_atl.rpy:270
    old "xpos 1.0 ypos .5"
    new ""

    # game/tutorial_atl.rpy:270
    old "xpos .75 ypos .25"
    new ""

    # game/tutorial_atl.rpy:270
    old "xpos .25 ypos .33"
    new ""

