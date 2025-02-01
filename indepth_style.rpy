﻿# TODO: Translation updated at 2025-01-26 12:26

# game/indepth_style.rpy:40
translate italian new_gui_17a0326e:

    # e "When you create a new project, Ren'Py will automatically create a GUI - a Graphical User Interface - for it."
    e ""

# game/indepth_style.rpy:42
translate italian new_gui_12c814ed:

    # e "It defines the look of both in-game interface, like this text box, and out-of-game interface like the main and game menus."
    e ""

# game/indepth_style.rpy:44
translate italian new_gui_0a2a73bb:

    # e "The default GUI is meant to be nice enough for a simple project. With a few small changes, it's what you're seeing in this game."
    e ""

# game/indepth_style.rpy:46
translate italian new_gui_22adf68e:

    # e "The GUI is also meant to be easy for an intermediate creator to customize. Customizing the GUI consists of changing the image files in the gui directory, and changing variables in gui.rpy."
    e ""

# game/indepth_style.rpy:48
translate italian new_gui_da21de30:

    # e "At the same time, even when customized, the default GUI might be too recognizable for an extremely polished game. That's why we've made it easy to totally replace."
    e ""

# game/indepth_style.rpy:50
translate italian new_gui_45765574:

    # e "We've put an extensive guide to customizing the GUI on the Ren'Py website. So if you want to learn more, visit the {a=https://www.renpy.org/doc/html/gui.html}GUI customization guide{/a}."
    e ""

# game/indepth_style.rpy:58
translate italian styles_fa345a38:

    # e "Ren'Py has a powerful style system that controls what displayables look like."
    e ""

# game/indepth_style.rpy:60
translate italian styles_6189ee12:

    # e "While the default GUI uses variables to provide styles with sensible defaults, if you're replacing the GUI or creating your own screens, you'll need to learn about styles yourself."
    e ""

# game/indepth_style.rpy:68
translate italian styles_menu_a4a6913e:

    # e "What would you like to know about styles?" nointeract
    e "" nointeract

# game/indepth_style.rpy:98
translate italian style_basics_9a79ef89:

    # e "Styles let a displayable look different from game to game, or even inside the same game."
    e ""

# game/indepth_style.rpy:103
translate italian style_basics_48777f2c:

    # e "Both of these buttons use the same displayables. But since different styles have been applied, the buttons look different from each other."
    e ""

# game/indepth_style.rpy:108
translate italian style_basics_57704d8c:

    # e "Styles are a combination of information from four different places."
    e ""

# game/indepth_style.rpy:121
translate italian style_basics_144731f6:

    # e "The first place Ren'Py can get style information from is part of a screen. Each displayable created by a screen can take a style name and style properties."
    e ""

# game/indepth_style.rpy:138
translate italian style_basics_67e48162:

    # e "When a screen displayable contains text, style properties prefixed with text_ apply to that text."
    e ""

# game/indepth_style.rpy:151
translate italian style_basics_03516b4a:

    # e "The next is as part of a displayable created in an image statement. Style properties are just arguments to the displayable."
    e ""

# game/indepth_style.rpy:160
translate italian style_basics_ccc0d1ca:

    # egreen "Style properties can also be given as arguments when defining a character."
    egreen ""

# game/indepth_style.rpy:162
translate italian style_basics_013ab314:

    # egreen "Arguments beginning with who_ are style properties applied to the character's name, while those beginning with what_ are applied to the character's dialogue."
    egreen ""

# game/indepth_style.rpy:164
translate italian style_basics_dbe80939:

    # egreen "Style properties that don't have a prefix are also applied to the character's name."
    egreen ""

# game/indepth_style.rpy:174
translate italian style_basics_ac6a8414:

    # e "Finally, there is the style statement, which creates or changes a named style. By giving Text the style argument, we tell it to use the blue_text style." id style_basics_ac6a8414
    e "" id style_basics_ac6a8414

# game/indepth_style.rpy:180
translate italian style_basics_3d9bdff7:

    # e "A style property can inherit from a parent. If a style property is not given in a style, it comes from the parent of that style."
    e ""

# game/indepth_style.rpy:182
translate italian style_basics_49c5fbfe:

    # e "By default the parent of the style has the same name, with the prefix up to the first underscore removed. If the style does not have an underscore in its name, 'default' is used." id style_basics_49c5fbfe
    e "" id style_basics_49c5fbfe

# game/indepth_style.rpy:184
translate italian style_basics_6ab170a3:

    # e "For example, blue_text inherits from text, which in turn inherits from default. The default style defines all properties, so it doesn't inherit from anything."
    e ""

# game/indepth_style.rpy:190
translate italian style_basics_f78117a7:

    # e "The parent can be explicitly changed by giving the style statement an 'is' clause. In this case, we're explictly setting the style to the parent of text."
    e ""

# game/indepth_style.rpy:194
translate italian style_basics_6007040b:

    # e "Each displayable has a default style name. By default, it's usually the lower-case displayable name, like 'text' for Text, or 'button' for buttons."
    e ""

# game/indepth_style.rpy:196
translate italian style_basics_35db9a05:

    # e "In a screen, a displayable can be given the style_prefix property to give a prefix for that displayable and its children." id style_basics_35db9a05
    e "" id style_basics_35db9a05

# game/indepth_style.rpy:198
translate italian style_basics_422a87f7:

    # e "For example, a text displayable with a style_prefix of 'help' will be given the style 'help_text'."
    e ""

# game/indepth_style.rpy:200
translate italian style_basics_bad2e207:

    # e "Lastly, when a displayable is a button, or inside a button, it can take style prefixes."
    e ""

# game/indepth_style.rpy:202
translate italian style_basics_22ed20a1:

    # e "The prefixes idle_, hover_, and insensitive_ are used when the button is unfocused, focused, and unfocusable."
    e ""

# game/indepth_style.rpy:204
translate italian style_basics_7a58037e:

    # e "These can be preceded by selected_ to change how the button looks when it represents a selected value or screen."
    e ""

# game/indepth_style.rpy:233
translate italian style_basics_0cdcb8c3:

    # e "This screen shows the style prefixes in action. You can click on a button to select it, or click outside to advance."
    e ""

# game/indepth_style.rpy:240
translate italian style_basics_aed05094:

    # e "Those are the basics of styles. If GUI customization isn't enough for you, styles let you customize just about everything in Ren'Py."
    e ""

# game/indepth_style.rpy:253
translate italian style_general_81f3c8ff:

    # e "The first group of style properties that we'll go over are the general style properties. These work with every displayable, or at least many different ones."
    e ""

# game/indepth_style.rpy:264
translate italian style_general_a8d99699:

    # e "Every displayable takes the position properties, which control where it can be placed on screen. Since I've already mentioned them, I won't repeat them here."
    e ""

# game/indepth_style.rpy:275
translate italian style_general_58d4a18f:

    # e "The xmaximum and ymaximum properties set the maximum width and height of the displayable, respectively. This will cause Ren'Py to shrink things, if possible."
    e ""

# game/indepth_style.rpy:277
translate italian style_general_cae9a39f:

    # e "Sometimes, the shrunken size will be smaller than the size given by xmaximum and ymaximum."
    e ""

# game/indepth_style.rpy:279
translate italian style_general_5928c24e:

    # e "Similarly, the xminimum and yminimum properties set the minimum width and height. If the displayable is smaller, Ren'Py will try to make it bigger."
    e ""

# game/indepth_style.rpy:289
translate italian style_general_35a8ee5e:

    # e "The xsize and ysize properties set the minimum and maximum size to the same value, fixing the size."
    e ""

# game/indepth_style.rpy:291
translate italian style_general_fcfb0640:

    # e "These only works for displayables than can be resized. Some displayables, like images, can't be made bigger or smaller."
    e ""

# game/indepth_style.rpy:299
translate italian style_general_cd5cc97c:

    # e "The area property takes a tuple - a parenthesis bounded list of four items. The first two give the position, and the second two the size."
    e ""

# game/indepth_style.rpy:308
translate italian style_general_e5a58f0b:

    # e "Finally, the alt property changes the text used by self-voicing for the hearing impaired."
    e ""

# game/indepth_style.rpy:335
translate italian style_text_fe457b8f:

    # e "The text style properties apply to text and input displayables."
    e ""

# game/indepth_style.rpy:337
translate italian style_text_7ab53f03:

    # e "Text displayables can be created implicitly or explicitly. For example, a textbutton creates a text displayable with a style ending in button_text."
    e ""

# game/indepth_style.rpy:339
translate italian style_text_6dd42a57:

    # e "These can also be set in gui.rpy by changing or defining variables with names like gui.button_text_size."
    e ""

# game/indepth_style.rpy:347
translate italian style_text_c689130e:

    # e "The bold style property makes the text bold. This can be done using an algorithm, rather than a different version of the font."
    e ""

# game/indepth_style.rpy:355
translate italian style_text_3420bfe4:

    # e "The color property changes the color of the text. It takes hex color codes, just like everything else in Ren'Py."
    e ""

# game/indepth_style.rpy:363
translate italian style_text_14bd6327:

    # e "The first_indent style property determines how far the first line is indented."
    e ""

# game/indepth_style.rpy:371
translate italian style_text_779ac517:

    # e "The font style property changes the font the text uses. Ren'Py takes TrueType and OpenType fonts, and you'll have to include the font file as part of your visual novel."
    e ""

# game/indepth_style.rpy:379
translate italian style_text_917e2bca:

    # e "The size property changes the size of the text."
    e ""

# game/indepth_style.rpy:388
translate italian style_text_1a46cd43:

    # e "The italic property makes the text italic. Again, this is better done with a font, but for short amounts of text Ren'Py can do it for you."
    e ""

# game/indepth_style.rpy:397
translate italian style_text_472f382d:

    # e "The justify property makes the text justified, lining all but the last line up on the left and the right side."
    e ""

# game/indepth_style.rpy:405
translate italian style_text_87b075f8:

    # e "The kerning property kerns the text. When it's negative, characters are closer together. When positive, characters are farther apart."
    e ""

# game/indepth_style.rpy:415
translate italian style_text_fe7dec14:

    # e "The line_leading and line_spacing properties put spacing before each line, and between lines, respectively."
    e ""

# game/indepth_style.rpy:424
translate italian style_text_aee9277a:

    # e "The outlines property puts outlines around text. This takes a list of tuples, which is a bit complicated."
    e ""

# game/indepth_style.rpy:426
translate italian style_text_b4c5190f:

    # e "But if you ignore the brackets and parenthesis, you have the width of the outline, the color, and then horizontal and vertical offsets."
    e ""

# game/indepth_style.rpy:434
translate italian style_text_5a0c2c02:

    # e "The rest_indent property controls the indentation of lines after the first one."
    e ""

# game/indepth_style.rpy:443
translate italian style_text_430c1959:

    # e "The textalign property controls the positioning of multiple lines of text inside the text displayable. For example, 0.5 means centered." id style_text_430c1959
    e "" id style_text_430c1959

# game/indepth_style.rpy:445
translate italian style_text_19aa0833:

    # e "It doesn't change the position of the text displayable itself. For that, you'll often want to set the textalign and xalign to the same value." id style_text_19aa0833
    e "" id style_text_19aa0833

# game/indepth_style.rpy:455
translate italian style_text_efc3c392:

    # e "When both textalign and xalign are set to 1.0, the text is properly right-justified." id style_text_efc3c392
    e "" id style_text_efc3c392

# game/indepth_style.rpy:464
translate italian style_text_43be63b9:

    # e "The underline property underlines the text."
    e ""

# game/indepth_style.rpy:471
translate italian style_text_343f6d34:

    # e "Those are the most common text style properties, but not the only ones. Here are a few more that you might need in special circumstances."
    e ""

# game/indepth_style.rpy:479
translate italian style_text_e7204a95:

    # e "By default, text in Ren'Py is antialiased, to smooth the edges. The antialias property can turn that off, and make the text a little more jagged."
    e ""

# game/indepth_style.rpy:487
translate italian style_text_a5316e4c:

    # e "The adjust_spacing property is a very subtle one, that only matters when a player resizes the window. When True, characters will be shifted a bit so the Text has the same relative spacing."
    e ""

# game/indepth_style.rpy:496
translate italian style_text_605d4e4a:

    # e "When False, the text won't jump around as much. But it can be a little wider or narrower based on screen size."
    e ""

# game/indepth_style.rpy:505
translate italian style_text_acf8a0e1:

    # e "The layout property has a few special values that control where lines are broken. The 'nobreak' value disables line breaks entirely, making the text wider."
    e ""

# game/indepth_style.rpy:516
translate italian style_text_785729cf:

    # e "When the layout property is set to 'subtitle', the line breaking algorithm is changed to try to make all lines even in length, as subtitles usually are."
    e ""

# game/indepth_style.rpy:524
translate italian style_text_9c26f218:

    # e "The strikethrough property draws a line through the text. It seems pretty unlikely you'd want to use this one."
    e ""

# game/indepth_style.rpy:534
translate italian style_text_c7229243:

    # e "The vertical style property places text in a vertical layout. It's meant for Asian languages with special fonts."
    e ""

# game/indepth_style.rpy:540
translate italian style_text_724bd5e0:

    # e "And those are the text style properties. There might be a lot of them, but we want to give you a lot of control over how you present text to your players."
    e ""

# game/indepth_style.rpy:580
translate italian style_button_300b6af5:

    # e "Next up, we have the window and button style properties. These apply to windows like the text window at the bottom of this screen and frames like the ones we show examples in."
    e ""

# game/indepth_style.rpy:582
translate italian style_button_255a18e4:

    # e "These properties also apply to buttons, in-game and out-of-game. To Ren'Py, a button is a window you can click."
    e ""

# game/indepth_style.rpy:593
translate italian style_button_9b53ce93:

    # e "I'll start off with this style, which everything will inherit from. To make our lives easier, it inherits from the default style, rather than the customized buttons in this game's GUI." id style_button_9b53ce93
    e "" id style_button_9b53ce93

# game/indepth_style.rpy:595
translate italian style_button_aece4a8c:

    # e "The first style property is the background property. It adds a background to a button or window. Since this is a button, idle and hover variants choose different backgrounds when focused." id style_button_aece4a8c
    e "" id style_button_aece4a8c

# game/indepth_style.rpy:597
translate italian style_button_b969f04a:

    # e "We also center the two buttons, using the xalign position property."
    e ""

# game/indepth_style.rpy:601
translate italian style_button_269ae069:

    # e "We've also customized the style of the button's text, using this style. It centers the text and makes it change color when hovered."
    e ""

# game/indepth_style.rpy:612
translate italian style_button_1009f3e1:

    # e "Without any padding around the text, the button looks odd. Ren'Py has padding properties that add space inside the button's background."
    e ""

# game/indepth_style.rpy:621
translate italian style_button_5bdfa45a:

    # e "More commonly used are the xpadding and ypadding style properties, which add the same padding to the left and right, or the top and bottom, respectively."
    e ""

# game/indepth_style.rpy:629
translate italian style_button_81283d42:

    # e "The margin style properties work the same way, except they add space outside the background. The full set exists: left_margin, right_margin, top_margin, bottom_margin, xmargin, and ymargin."
    e ""

# game/indepth_style.rpy:638
translate italian style_button_0b7aca6b:

    # e "The size_group style property takes a string. Ren'Py will make sure that all the windows or buttons with the same size_group string are the same size."
    e ""

# game/indepth_style.rpy:647
translate italian style_button_4c6da7d9:

    # e "Alternatively, the xfill and yfill style properties make a button take up all available space in the horizontal or vertical directions."
    e ""

# game/indepth_style.rpy:657
translate italian style_button_fd5338b2:

    # e "The foreground property gives a displayable that is placed on top of the contents and background of the window or button."
    e ""

# game/indepth_style.rpy:659
translate italian style_button_b8af697c:

    # e "One way to use it is to provide extra decorations to a button that's serving as a checkbox. Another would be to use it with a Frame to provide a glossy shine that overlays the button's contents."
    e ""

# game/indepth_style.rpy:668
translate italian style_button_c0b1b62e:

    # e "There are also a few style properties that only apply to buttons. The hover_sound and activate_sound properties play sound files when a button is focused and activated, respectively."
    e ""

# game/indepth_style.rpy:677
translate italian style_button_02fa647e:

    # e "Finally, the focus_mask property applies to partially transparent buttons. When it's set to True, only areas of the button that aren't transparent cause a button to focus."
    e ""

# game/indepth_style.rpy:757
translate italian style_bar_414d454a:

    # e "To demonstrate styles, let me first show two of the images we'll be using. This is the image we're using for parts of the bar that are empty."
    e ""

# game/indepth_style.rpy:761
translate italian style_bar_9422b7b0:

    # e "And here's what we use for parts of the bar that are full."
    e ""

# game/indepth_style.rpy:773
translate italian style_bar_8ae6a14b:

    # e "The left_bar and right_bar style properties, and their hover variants, give displayables for the left and right side of the bar. By default, the value is shown on the left."
    e ""

# game/indepth_style.rpy:775
translate italian style_bar_7f0f50e5:

    # e "Also by default, both the left and right displayables are rendered at the full width of the bar, and then cropped to the appropriate size."
    e ""

# game/indepth_style.rpy:777
translate italian style_bar_9ef4f62f:

    # e "We give the bar the ysize property to set how tall it is. We could also give it xsize to choose how wide, but here it's limited by the width of the frame it's in."
    e ""

# game/indepth_style.rpy:790
translate italian style_bar_d4c29710:

    # e "When the bar_invert style property is True, the bar value is displayed on the right side of the bar. The left_bar and right_bar displayables might also need to be swapped."
    e ""

# game/indepth_style.rpy:804
translate italian style_bar_cca67222:

    # e "The bar_resizing style property causes the bar images to be resized to represent the value, rather than being rendered at full size and cropped."
    e ""

# game/indepth_style.rpy:817
translate italian style_bar_7d361bac:

    # e "The thumb style property gives a thumb image, that's placed based on the bar's value. In the case of a scrollbar, it's resized if possible." id style_bar_7d361bac
    e "" id style_bar_7d361bac

# game/indepth_style.rpy:819
translate italian style_bar_b6dfb61b:

    # e "Here, we use it with the base_bar style property, which sets both bar images to the same displayable."
    e ""

# game/indepth_style.rpy:834
translate italian style_bar_996466ad:

    # e "The left_gutter and right_gutter properties set a gutter on the left or right size of the bar. The gutter is space the bar can't be dragged into, that can be used for borders."
    e ""

# game/indepth_style.rpy:849
translate italian style_bar_fa41a83c:

    # e "The bar_vertical style property displays a vertically oriented bar. All of the other properties change names - left_bar becomes top_bar, while right_bar becomes bottom_bar."
    e ""

# game/indepth_style.rpy:854
translate italian style_bar_5d33c5dc:

    # e "Finally, there's one style we can't show here, and it's unscrollable. It controls what happens when a scrollbar can't be moved at all."
    e ""

# game/indepth_style.rpy:856
translate italian style_bar_e8e32280:

    # e "By default, it's shown. But if unscrollable is 'insensitive', the bar becomes insensitive. If it's 'hide', the bar is hidden, but still takes up space."
    e ""

# game/indepth_style.rpy:860
translate italian style_bar_f1292000:

    # e "That's it for the bar properties. By using them, a creator can customize bars, scrollbars, and sliders."
    e ""

# game/indepth_style.rpy:959
translate italian style_box_5fd535f4:

    # e "The hbox displayable is used to lay its children out horizontally. By default, there's no spacing between children, so they run together."
    e ""

# game/indepth_style.rpy:965
translate italian style_box_0111e5dc:

    # e "Similarly, the vbox displayable is used to lay its children out vertically. Both support style properties that control placement."
    e ""

# game/indepth_style.rpy:970
translate italian style_box_5a44717b:

    # e "To make the size of the box displayable obvious, I'll add a highlight to the box itself, and not the frame containing it."
    e ""

# game/indepth_style.rpy:978
translate italian style_box_239e7a8f:

    # e "Boxes support the xfill and yfill style properties. These properties make a box expand to fill the available space, rather than the space of the largest child."
    e ""

# game/indepth_style.rpy:988
translate italian style_box_e513c946:

    # e "The spacing style property takes a value in pixels, and adds that much spacing between each child of the box."
    e ""

# game/indepth_style.rpy:998
translate italian style_box_6ae4f94d:

    # e "The first_spacing style property is similar, but it only adds space between the first and second children. This is useful when the first child is a title that needs different spacing."
    e ""

# game/indepth_style.rpy:1008
translate italian style_box_0c518d9f:

    # e "The box_reverse style property reverses the order of entries in the box."
    e ""

# game/indepth_style.rpy:1021
translate italian style_box_f73c1422:

    # e "We'll switch back to a horizontal box for our next example."
    e ""

# game/indepth_style.rpy:1031
translate italian style_box_285592bb:

    # e "The box_wrap style property fills the box with children until it's full, then starts again on the next line."
    e ""

# game/indepth_style.rpy:1044
translate italian style_box_a7637552:

    # e "Grids bring with them two more style properties. The xspacing and yspacing properties control spacing in the horizontal and vertical directions, respectively."
    e ""

# game/indepth_style.rpy:1051
translate italian style_box_4006f74b:

    # e "Lastly, we have the fixed layout. The fixed layout usually expands to fill all space, and shows its children from back to front."
    e ""

# game/indepth_style.rpy:1053
translate italian style_box_4a2866f0:

    # e "But of course, we have some style properties that can change that."
    e ""

# game/indepth_style.rpy:1062
translate italian style_box_66e042c4:

    # e "When the xfit style property is True, the fixed lays out all its children as if it was full size, and then shrinks in width to fit them. The yfit style works the same way, but in height."
    e ""

# game/indepth_style.rpy:1070
translate italian style_box_6a593b10:

    # e "The order_reverse style property changes the order in which the children are shown. Instead of back-to-front, they're displayed front-to-back."
    e ""

# game/indepth_style.rpy:1082
translate italian style_inspector_21bc0709:

    # e "Sometimes it's hard to figure out what style is being used for a particular displayable. The displayable inspector can help with that."
    e ""

# game/indepth_style.rpy:1084
translate italian style_inspector_243c50f0:

    # e "To use it, place the mouse over a portion of the Ren'Py user interface, and hit shift+I. That's I for inspector."
    e ""

# game/indepth_style.rpy:1086
translate italian style_inspector_bcbdc396:

    # e "Ren'Py will pop up a list of displayables the mouse is over. Next to each is the name of the style that displayable uses."
    e ""

# game/indepth_style.rpy:1088
translate italian style_inspector_d981e5c8:

    # e "You can click on the name of the style to see where it gets its properties from."
    e ""

# game/indepth_style.rpy:1090
translate italian style_inspector_ef46b86d:

    # e "By default, the inspector only shows interface elements like screens, and not images. Type shift+alt+I if you'd like to see images as well."
    e ""

# game/indepth_style.rpy:1092
translate italian style_inspector_b59c6b69:

    # e "You can try the inspector right now, by hovering this text and hitting shift+I."
    e ""

translate italian strings:

    # game/indepth_style.rpy:20
    old "Button 1"
    new ""

    # game/indepth_style.rpy:22
    old "Button 2"
    new ""

    # game/indepth_style.rpy:66
    old "Style basics."
    new ""

    # game/indepth_style.rpy:66
    old "General style properties."
    new ""

    # game/indepth_style.rpy:66
    old "Text style properties."
    new ""

    # game/indepth_style.rpy:66
    old "Window and Button style properties."
    new ""

    # game/indepth_style.rpy:66
    old "Bar style properties."
    new ""

    # game/indepth_style.rpy:66
    old "Box, Grid, and Fixed style properties."
    new ""

    # game/indepth_style.rpy:66
    old "The Displayable Inspector."
    new ""

    # game/indepth_style.rpy:66
    old "That's all I want to know."
    new ""

    # game/indepth_style.rpy:112
    old "This text is colored green."
    new ""

    # game/indepth_style.rpy:126
    old "Danger"
    new ""

    # game/indepth_style.rpy:142
    old "This text is colored red."
    new ""

    # game/indepth_style.rpy:170
    old "This text is colored blue."
    new ""

    # game/indepth_style.rpy:248
    old "Orbiting Earth in the spaceship, I saw how beautiful our planet is.\n–Yuri Gagarin"
    new ""

    # game/indepth_style.rpy:303
    old "\"Orbiting Earth in the spaceship, I saw how beautiful our planet is.\" Said by Yuri Gagarin."
    new ""

    # game/indepth_style.rpy:326
    old "Vertical"
    new ""

    # game/indepth_style.rpy:329
    old "Far better it is to dare mighty things, to win glorious triumphs, even though checkered by failure, than to rank with those poor spirits who neither enjoy nor suffer much, because they live in the gray twilight that knows not victory nor defeat.\n\n–Theodore Roosevelt"
    new ""

    # game/indepth_style.rpy:561
    old "Top Choice"
    new ""

    # game/indepth_style.rpy:566
    old "Bottom Choice"
    new ""

    # game/indepth_style.rpy:877
    old "First Child"
    new ""

    # game/indepth_style.rpy:878
    old "Second Child"
    new ""

    # game/indepth_style.rpy:879
    old "Third Child"
    new ""

    # game/indepth_style.rpy:882
    old "Fourth Child"
    new ""

    # game/indepth_style.rpy:883
    old "Fifth Child"
    new ""

    # game/indepth_style.rpy:884
    old "Sixth Child"
    new ""

