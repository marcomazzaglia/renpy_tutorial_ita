# TODO: Translation updated at 2025-01-26 12:26

# game/tutorial_screen_displayables.rpy:3
translate italian screen_displayables_7c897a6d:

    # e "There are quite a few screen displayables. Here, I'll tell you about some of the most important ones."
    e "Ci sono parecchi screen displayable. Qui ti parlerò di alcuni dei più importanti."

# game/tutorial_screen_displayables.rpy:11
translate italian screen_displayables_menu_fef7b441:

    # e "What would you like to know about?" nointeract
    e "Di cosa vorresti sapere?" nointeract

# game/tutorial_screen_displayables.rpy:49
translate italian screen_displayable_properties_76c5639a:

    # e "There are a few properties that every screen language displayable shares. Here, I'll demonstrate them for you."
    e "Ci sono alcune proprietà che ogni displayable del linguaggio screen condivide. Qui te le dimostrerò."

# game/tutorial_screen_displayables.rpy:57
translate italian screen_displayable_properties_527d4b4e:

    # e "First off, every screen language displayable supports the position properties. When the container a displayable is in supports it, you can use properties like align, anchor, pos, and so so on."
    e "Prima di tutto, ogni displayable del linguaggio screen supporta le proprietà di posizione. Quando il contenitore in cui si trova un displayable lo supporta, puoi usare proprietà come align, anchor, pos, e così via."

# game/tutorial_screen_displayables.rpy:69
translate italian screen_displayable_properties_8aff26dd:

    # e "The at property applies a transform to the displayable, the same way the at clause in the show statement does."
    e "La proprietà at applica una trasformazione al displayable, allo stesso modo in cui lo fa la clausola at nell'istruzione show."

# game/tutorial_screen_displayables.rpy:106
translate italian screen_displayable_properties_2ed40a70:

    # e "The id property is mostly used with the say screen, which is used to show dialogue. Outside of the say screen, it isn't used much."
    e "La proprietà id viene usata principalmente con lo screen say, che viene usato per mostrare il dialogo. Al di fuori dello screen say, non viene usata molto."

# game/tutorial_screen_displayables.rpy:108
translate italian screen_displayable_properties_da5733d1:

    # e "It tells Ren'Py which displayables are the background window, 'who' is speaking, and 'what' is being said. This used to apply per-Character styles, and help with auto-forward mode."
    e "Dice a Ren'Py quali displayable sono la finestra di sfondo, 'chi' sta parlando e 'cosa' viene detto. Questo serviva per applicare stili per-Personaggio e aiutare con la modalità avanzamento automatico."

# game/tutorial_screen_displayables.rpy:123
translate italian screen_displayable_properties_cc09fade:

    # e "The style property lets you specify the style of a single displayable."
    e "La proprietà style ti permette di specificare lo stile di un singolo displayable."

# game/tutorial_screen_displayables.rpy:144
translate italian screen_displayable_properties_a7f4e25c:

    # e "The style_prefix property sets the prefix of the style that's used for a displayable and its children."
    e "La proprietà style_prefix imposta il prefisso dello stile che viene usato per un displayable e i suoi figli."

# game/tutorial_screen_displayables.rpy:146
translate italian screen_displayable_properties_6bdb0723:

    # e "For example, when the style_prefix property is 'green', the vbox has the 'green_vbox' style, and the text in it has the 'green_text' style."
    e "Per esempio, quando la proprietà style_prefix è 'green', il vbox ha lo stile 'green_vbox' e il testo al suo interno ha lo stile 'green_text'."

# game/tutorial_screen_displayables.rpy:150
translate italian screen_displayable_properties_8a3a8635:

    # e "There are a few more properties than these, and you can find the rest in the documentation. But these are the ones you can expect to see in your game, in the default screens."
    e "Ci sono alcune proprietà in più di queste, e puoi trovare le altre nella documentazione. Ma queste sono quelle che puoi aspettarti di vedere nel tuo gioco, negli screen predefiniti."

# game/tutorial_screen_displayables.rpy:156
translate italian add_displayable_ec121c5c:

    # e "Sometimes you'll have a displayable, like an image, that you want to add to a screen."
    e "A volte avrai un displayable, come un'immagine, che vuoi aggiungere a uno screen."

# game/tutorial_screen_displayables.rpy:165
translate italian add_displayable_7ec3e2b0:

    # e "This can be done using the add statement, which adds an image or other displayable to the screen."
    e "Questo può essere fatto usando l'istruzione add, che aggiunge un'immagine o altro displayable allo screen."

# game/tutorial_screen_displayables.rpy:167
translate italian add_displayable_7112a377:

    # e "There are a few ways to refer to the image. If it's in the images directory or defined with the image statement, you can just put the name inside a quoted string."
    e "Ci sono alcuni modi per riferirsi all'immagine. Se è nella directory images o definita con l'istruzione image, puoi semplicemente mettere il nome dentro una stringa tra virgolette."

# game/tutorial_screen_displayables.rpy:176
translate italian add_displayable_8ba81c26:

    # e "An image can also be referred to by its filename, relative to the game directory." id add_displayable_8ba81c26
    e "Un'immagine può anche essere riferita tramite il suo nome file, relativo alla directory del gioco." id add_displayable_8ba81c26

# game/tutorial_screen_displayables.rpy:185
translate italian add_displayable_1f5571e3:

    # e "Other displayables can also be added using the add statement. Here, we add the Solid displayable, showing a solid block of color."
    e "Altri displayable possono anche essere aggiunti usando l'istruzione add. Qui aggiungiamo il displayable Solid, mostrando un blocco solido di colore."

# game/tutorial_screen_displayables.rpy:195
translate italian add_displayable_0213ffa2:

    # e "In addition to the displayable, the add statement can be given transform properties. These can place or otherwise transform the displayable being added."
    e "Oltre al displayable, all'istruzione add possono essere date proprietà di trasformazione. Queste possono posizionare o altrimenti trasformare il displayable che viene aggiunto."

# game/tutorial_screen_displayables.rpy:207
translate italian add_displayable_3a56a464:

    # e "Of course, the add statement can also take the at property, letting you give it a more complex transform."
    e "Ovviamente, l'istruzione add può anche prendere la proprietà at, permettendoti di darle una trasformazione più complessa."

# game/tutorial_screen_displayables.rpy:222
translate italian text_displayable_96f88225:

    # e "The screen language text statement adds a text displayable to the screen. It takes one argument, the text to be displayed."
    e "L'istruzione text del linguaggio screen aggiunge un displayable di testo allo screen. Prende un argomento, il testo da visualizzare."

# game/tutorial_screen_displayables.rpy:224
translate italian text_displayable_1ed1a8c2:

    # e "In addition to the common properties that all displayables take, text takes the text style properties. For example, size sets the size of the text."
    e "Oltre alle proprietà comuni che tutti i displayable prendono, text prende le proprietà di stile del testo. Per esempio, size imposta la dimensione del testo."

# game/tutorial_screen_displayables.rpy:234
translate italian text_displayable_9351d9dd:

    # e "The text displayable can also interpolate values enclosed in square brackets."
    e "Il displayable text può anche interpolare valori racchiusi tra parentesi quadre."

# game/tutorial_screen_displayables.rpy:236
translate italian text_displayable_32d76ccb:

    # e "When text is displayed in a screen using the text statement, variables defined in the screen take precedence over those defined outside it." id text_displayable_32d76ccb
    e "Quando il testo viene visualizzato in uno screen usando l'istruzione text, le variabili definite nello screen hanno la precedenza su quelle definite al di fuori." id text_displayable_32d76ccb

# game/tutorial_screen_displayables.rpy:238
translate italian text_displayable_7e84a5d1:

    # e "Those variables may be parameters given to the screen, defined with the default or python statements, or set using the SetScreenVariable action."
    e "Quelle variabili possono essere parametri dati allo screen, definiti con le istruzioni default o python, o impostati usando l'azione SetScreenVariable."

# game/tutorial_screen_displayables.rpy:247
translate italian text_displayable_8bc866c4:

    # e "There's not much more to say about text in screens, as it works the same way as all other text in Ren'Py."
    e "Non c'è molto altro da dire sul testo negli screen, poiché funziona allo stesso modo di tutto l'altro testo in Ren'Py."

# game/tutorial_screen_displayables.rpy:255
translate italian layout_displayables_d75efbae:

    # e "The layout displayables take other displayables and lay them out on the screen."
    e "I displayable di layout prendono altri displayable e li dispongono sullo schermo."

# game/tutorial_screen_displayables.rpy:269
translate italian layout_displayables_9a15144d:

    # e "For example, the hbox displayable takes its children and lays them out horizontally."
    e "Per esempio, il displayable hbox prende i suoi figli e li dispone orizzontalmente."

# game/tutorial_screen_displayables.rpy:284
translate italian layout_displayables_48eff197:

    # e "The vbox displayable is similar, except it takes its children and arranges them vertically."
    e "Il displayable vbox è simile, tranne che prende i suoi figli e li dispone verticalmente."

# game/tutorial_screen_displayables.rpy:286
translate italian layout_displayables_74de8a66:

    # e "Both of the boxes take the box style properties, the most useful of which is spacing, the amount of space to leave between children."
    e "Entrambe le scatole prendono le proprietà di stile box, la più utile delle quali è spacing, la quantità di spazio da lasciare tra i figli."

# game/tutorial_screen_displayables.rpy:301
translate italian layout_displayables_a156591f:

    # e "The grid displayable displays its children in a grid of equally-sized cells. It takes two arguments, the number of columns and the number of rows."
    e "Il displayable grid visualizza i suoi figli in una griglia di celle di dimensioni uguali. Prende due argomenti, il numero di colonne e il numero di righe."

# game/tutorial_screen_displayables.rpy:303
translate italian layout_displayables_126f5816:

    # e "The grid has to be full, or Ren'Py will produce an error. Notice how in this example, the empty cell is filled with a null."
    e "La griglia deve essere piena, altrimenti Ren'Py produrrà un errore. Nota come in questo esempio, la cella vuota è riempita con un null."

# game/tutorial_screen_displayables.rpy:305
translate italian layout_displayables_bfaaaf9b:

    # e "Like the boxes, grid uses the spacing property to specify the space between cells."
    e "Come le scatole, grid usa la proprietà spacing per specificare lo spazio tra le celle."

# game/tutorial_screen_displayables.rpy:321
translate italian layout_displayables_3e931106:

    # e "Grid also takes the transpose property, to make it fill top-to-bottom before it fills left-to-right."
    e "Grid prende anche la proprietà transpose, per farla riempire dall'alto verso il basso prima di riempirla da sinistra a destra."

# game/tutorial_screen_displayables.rpy:338
translate italian layout_displayables_afdc1b11:

    # e "And just to demonstrate that all cells are equally-sized, here's what happens when once child is bigger than the others."
    e "E solo per dimostrare che tutte le celle sono di dimensioni uguali, ecco cosa succede quando un figlio è più grande degli altri."

# game/tutorial_screen_displayables.rpy:353
translate italian layout_displayables_a23e2826:

    # e "The fixed displayable displays the children using Ren'Py's normal placement algorithm. This lets you place displayables anywhere in the screen."
    e "Il displayable fixed visualizza i figli usando l'algoritmo di posizionamento normale di Ren'Py. Questo ti permette di posizionare i displayable ovunque nello screen."

# game/tutorial_screen_displayables.rpy:355
translate italian layout_displayables_fd3926ca:

    # e "By default, the layout expands to fill all the space available to it. To prevent that, we use the xsize and ysize properties to set its size in advance."
    e "Per impostazione predefinita, il layout si espande per riempire tutto lo spazio disponibile. Per evitarlo, usiamo le proprietà xsize e ysize per impostarne la dimensione in anticipo."

# game/tutorial_screen_displayables.rpy:369
translate italian layout_displayables_eff42786:

    # e "When a non-layout displayable is given two or more children, it's not necessary to create a fixed. A fixed is automatically added, and the children are added to it."
    e "Quando a un displayable non-layout vengono dati due o più figli, non è necessario creare un fixed. Un fixed viene aggiunto automaticamente e i figli vengono aggiunti ad esso."

# game/tutorial_screen_displayables.rpy:384
translate italian layout_displayables_c32324a7:

    # e "Finally, there's one convenience to save space. When many displayables are nested, adding a layout to each could cause crazy indent levels."
    e "Infine, c'è una comodità per risparmiare spazio. Quando molti displayable sono annidati, aggiungere un layout a ciascuno potrebbe causare livelli di indentazione folli."

# game/tutorial_screen_displayables.rpy:386
translate italian layout_displayables_d7fa0f28:

    # e "The has statement creates a layout, and then adds all further children of its parent to that layout. It's just a convenience to make screens more readable."
    e "L'istruzione has crea un layout e poi aggiunge tutti i figli successivi del suo genitore a quel layout. È solo una comodità per rendere gli screen più leggibili."

# game/tutorial_screen_displayables.rpy:395
translate italian window_displayables_14beb786:

    # e "In the default GUI that Ren'Py creates for a game, most user interface elements expect some sort of background."
    e "Nella GUI predefinita che Ren'Py crea per un gioco, la maggior parte degli elementi dell'interfaccia utente si aspetta una qualche forma di sfondo."

# game/tutorial_screen_displayables.rpy:405
translate italian window_displayables_495d332b:

    # e "Without the background, text can be hard to read. While a frame isn't strictly required, many screens have one or more of them."
    e "Senza lo sfondo, il testo può essere difficile da leggere. Mentre un frame non è strettamente richiesto, molti screen ne hanno uno o più."

# game/tutorial_screen_displayables.rpy:417
translate italian window_displayables_2c0565ab:

    # e "But when I add a background, it's much easier. That's why there are two displayables that are intended to give backgrounds to user interface elements."
    e "Ma quando aggiungo uno sfondo, è molto più facile. Ecco perché ci sono due displayable che sono destinati a dare sfondi agli elementi dell'interfaccia utente."

# game/tutorial_screen_displayables.rpy:419
translate italian window_displayables_c7d0968c:

    # e "The two displayables are frame and window. Frame is the one we use above, and it's designed to provide a background for arbitrary parts of the user interface."
    e "I due displayable sono frame e window. Frame è quello che usiamo sopra, ed è progettato per fornire uno sfondo per parti arbitrarie dell'interfaccia utente."

# game/tutorial_screen_displayables.rpy:423
translate italian window_displayables_7d843f62:

    # e "On the other hand, the window displayable is very specific. It's used to provide the text window. If you're reading what I'm saying, you're looking at the text window right now."
    e "D'altra parte, il displayable window è molto specifico. Viene usato per fornire la finestra di testo. Se stai leggendo quello che sto dicendo, stai guardando la finestra di testo proprio ora."

# game/tutorial_screen_displayables.rpy:425
translate italian window_displayables_de5963e4:

    # e "Both frames and windows can be given window style properties, allowing you to change things like the background, margins, and padding around the window."
    e "Sia i frame che le finestre possono ricevere proprietà di stile window, permettendoti di cambiare cose come lo sfondo, i margini e il padding attorno alla finestra."

# game/tutorial_screen_displayables.rpy:433
translate italian button_displayables_ea626553:

    # e "One of the most flexible displayables is the button displayable, and its textbutton and imagebutton variants."
    e "Uno dei displayable più flessibili è il displayable button, e le sue varianti textbutton e imagebutton."

# game/tutorial_screen_displayables.rpy:443
translate italian button_displayables_372dcc0f:

    # e "A button is a displayable that when selected runs an action. Buttons can be selected by clicking with the mouse, by touch, or with the keyboard and controller."
    e "Un pulsante è un displayable che quando viene selezionato esegue un'azione. I pulsanti possono essere selezionati cliccando con il mouse, tramite tocco, o con la tastiera e il controller."

# game/tutorial_screen_displayables.rpy:445
translate italian button_displayables_a6b270ff:

    # e "Actions can do many things, like setting variables, showing screens, jumping to a label, or returning a value. There are many {a=https://www.renpy.org/doc/html/screen_actions.html}actions in the Ren'Py documentation{/a}, and you can also write your own."
    e "Le azioni possono fare molte cose, come impostare variabili, mostrare screen, saltare a un'etichetta o restituire un valore. Ci sono molte {a=https://www.renpy.org/doc/html/screen_actions.html}azioni nella documentazione di Ren'Py{/a}, e puoi anche scrivere le tue."

# game/tutorial_screen_displayables.rpy:458
translate italian button_displayables_4c600d20:

    # e "It's also possible to run actions when a button gains and loses focus."
    e "È anche possibile eseguire azioni quando un pulsante ottiene e perde il focus."

# game/tutorial_screen_displayables.rpy:473
translate italian button_displayables_47af4bb9:

    # e "A button takes another displayable as a child. Since that child can be a layout, it can take as many children as you want." id button_displayables_47af4bb9
    e "Un pulsante prende un altro displayable come figlio. Poiché quel figlio può essere un layout, può prendere quanti figli vuoi." id button_displayables_47af4bb9

# game/tutorial_screen_displayables.rpy:483
translate italian button_displayables_d01adde3:

    # e "In many cases, buttons will be given text. To make that easier, there's the textbutton displayable that takes the text as an argument."
    e "In molti casi, ai pulsanti verrà dato del testo. Per renderlo più facile, c'è il displayable textbutton che prende il testo come argomento."

# game/tutorial_screen_displayables.rpy:485
translate italian button_displayables_01c551b3:

    # e "Since the textbutton displayable manages the style of the button text for you, it's the kind of button that's used most often in the default GUI."
    e "Poiché il displayable textbutton gestisce lo stile del testo del pulsante per te, è il tipo di pulsante usato più spesso nella GUI predefinita."

# game/tutorial_screen_displayables.rpy:498
translate italian button_displayables_6911fb9b:

    # e "There's also the imagebutton, which takes displayables, one for each state the button can be in, and displays them as the button."
    e "C'è anche l'imagebutton, che prende displayable, uno per ogni stato in cui può trovarsi il pulsante, e li visualizza come pulsante."

# game/tutorial_screen_displayables.rpy:500
translate italian button_displayables_49720fa6:

    # e "An imagebutton gives you the most control over what a button looks like, but is harder to translate and won't look as good if the game window is resized."
    e "Un imagebutton ti dà il massimo controllo su come appare un pulsante, ma è più difficile da tradurre e non sembrerà bello se la finestra del gioco viene ridimensionata."

# game/tutorial_screen_displayables.rpy:522
translate italian button_displayables_e8d40fc8:

    # e "Buttons take Window style properties, that are used to specify the background, margins, and padding. They also take Button-specific properties, like a sound to play on hover."
    e "I pulsanti prendono proprietà di stile Window, che vengono usate per specificare lo sfondo, i margini e il padding. Prendono anche proprietà specifiche dei pulsanti, come un suono da riprodurre al passaggio del mouse."

# game/tutorial_screen_displayables.rpy:524
translate italian button_displayables_1e40e311:

    # e "When used with a button, style properties can be given prefixes like idle and hover to make the property change with the button state."
    e "Quando usate con un pulsante, le proprietà di stile possono ricevere prefissi come idle e hover per far cambiare la proprietà con lo stato del pulsante."

# game/tutorial_screen_displayables.rpy:526
translate italian button_displayables_220b020d:

    # e "A text button also takes Text style properties, prefixed with text. These are applied to the text displayable it creates internally."
    e "Un pulsante di testo prende anche proprietà di stile Text, con prefisso text. Queste vengono applicate al displayable text che crea internamente."

# game/tutorial_screen_displayables.rpy:558
translate italian button_displayables_b89d12aa:

    # e "Of course, it's prety rare we'd ever customize a button in a screen like that. Instead, we'd create custom styles and tell Ren'Py to use them."
    e "Ovviamente, è piuttosto raro che personalizzeremmo mai un pulsante in uno screen in quel modo. Invece, creeremmo stili personalizzati e diremmo a Ren'Py di usarli."

# game/tutorial_screen_displayables.rpy:577
translate italian bar_displayables_946746c2:

    # e "The bar and vbar displayables are flexible displayables that show bars representing a value. The value can be static, animated, or adjustable by the player."
    e "I displayable bar e vbar sono displayable flessibili che mostrano barre che rappresentano un valore. Il valore può essere statico, animato o regolabile dal giocatore."

# game/tutorial_screen_displayables.rpy:579
translate italian bar_displayables_af3a51b8:

    # e "The value property gives a BarValue, which is an object that determines the bar's value and range. Here, a StaticValue sets the range to 100 and the value to 66, making a bar that's two thirds full."
    e "La proprietà value fornisce un BarValue, che è un oggetto che determina il valore e l'intervallo della barra. Qui, uno StaticValue imposta l'intervallo a 100 e il valore a 66, creando una barra piena per due terzi."

# game/tutorial_screen_displayables.rpy:581
translate italian bar_displayables_62f8b0ab:

    # e "A list of all the BarValues that can be used is found {a=https://www.renpy.org/doc/html/screen_actions.html#bar-values}in the Ren'Py documentation{/a}."
    e "Un elenco di tutti i BarValue che possono essere usati si trova {a=https://www.renpy.org/doc/html/screen_actions.html#bar-values}nella documentazione di Ren'Py{/a}."

# game/tutorial_screen_displayables.rpy:583
translate italian bar_displayables_5212eb0a:

    # e "In this example, we give the frame the xsize property. If we didn't do that, the bar would expand to fill all available horizontal space."
    e "In questo esempio, diamo al frame la proprietà xsize. Se non lo facessimo, la barra si espanderebbe per riempire tutto lo spazio orizzontale disponibile."

# game/tutorial_screen_displayables.rpy:600
translate italian bar_displayables_67295018:

    # e "There are a few different bar styles that are defined in the default GUI. The styles are selected by the style property, with the default selected by the value."
    e "Ci sono alcuni stili di barra diversi che sono definiti nella GUI predefinita. Gli stili sono selezionati dalla proprietà style, con il default selezionato dal valore."

# game/tutorial_screen_displayables.rpy:602
translate italian bar_displayables_1b037b21:

    # e "The top style is the 'bar' style. It's used to display values that the player can't adjust, like a life or progress bar."
    e "Lo stile superiore è lo stile 'bar'. Viene usato per visualizzare valori che il giocatore non può regolare, come una barra della vita o del progresso."

# game/tutorial_screen_displayables.rpy:604
translate italian bar_displayables_c2aa4725:

    # e "The middle style is the 'slider' value. It's used for values the player is expected to adjust, like a volume preference." id bar_displayables_c2aa4725
    e "Lo stile intermedio è il valore 'slider'. Viene usato per valori che il giocatore dovrebbe regolare, come una preferenza di volume." id bar_displayables_c2aa4725

# game/tutorial_screen_displayables.rpy:606
translate italian bar_displayables_2fc44226:

    # e "Finally, the bottom style is the 'scrollbar' style, which is used for horizontal scrollbars. When used as a scrollbar, the thumb in the center changes size to reflect the visible area of a viewport."
    e "Infine, lo stile inferiore è lo stile 'scrollbar', che viene usato per le barre di scorrimento orizzontali. Quando usato come barra di scorrimento, il cursore al centro cambia dimensione per riflettere l'area visibile di un viewport."

# game/tutorial_screen_displayables.rpy:623
translate italian bar_displayables_26eb88bf:

    # e "The vbar displayable is similar to the bar displayable, except it uses vertical styles - 'vbar', 'vslider', and 'vscrollbar' - by default."
    e "Il displayable vbar è simile al displayable bar, tranne che usa stili verticali - 'vbar', 'vslider' e 'vscrollbar' - per impostazione predefinita."

# game/tutorial_screen_displayables.rpy:626
translate italian bar_displayables_11cf8af2:

    # e "Bars take the Bar style properties, which can customize the look and feel greatly. Just look at the difference between the bar, slider, and scrollbar styles."
    e "Le barre prendono le proprietà di stile Bar, che possono personalizzare notevolmente l'aspetto. Guarda solo la differenza tra gli stili bar, slider e scrollbar."

# game/tutorial_screen_displayables.rpy:635
translate italian imagemap_displayables_d62fad02:

    # e "Imagemaps use two or more images to show buttons and bars. Let me start by showing you an example of an imagemap in action."
    e "Le imagemap usano due o più immagini per mostrare pulsanti e barre. Lascia che inizi mostrandoti un esempio di imagemap in azione."

# game/tutorial_screen_displayables.rpy:657
translate italian swimming_405542a5:

    # e "You chose swimming."
    e "Hai scelto il nuoto."

# game/tutorial_screen_displayables.rpy:659
translate italian swimming_264b5873:

    # e "Swimming seems like a lot of fun, but I didn't bring my bathing suit with me."
    e "Il nuoto sembra molto divertente, ma non ho portato il mio costume da bagno con me."

# game/tutorial_screen_displayables.rpy:665
translate italian science_83e5c0cc:

    # e "You chose science."
    e "Hai scelto la scienza."

# game/tutorial_screen_displayables.rpy:667
translate italian science_319cdf4b:

    # e "I've heard that some schools have a competitive science team, but to me research is something that can't be rushed."
    e "Ho sentito che alcune scuole hanno un team scientifico competitivo, ma per me la ricerca è qualcosa che non può essere affrettata."

# game/tutorial_screen_displayables.rpy:672
translate italian art_d2a94440:

    # e "You chose art."
    e "Hai scelto l'arte."

# game/tutorial_screen_displayables.rpy:674
translate italian art_e6af6f1d:

    # e "Really good background art is hard to make, which is why so many games use filtered photographs. Maybe you can change that."
    e "L'arte di sfondo davvero buona è difficile da realizzare, ed è per questo che così tanti giochi usano fotografie filtrate. Forse puoi cambiare questo."

# game/tutorial_screen_displayables.rpy:680
translate italian home_373ea9a5:

    # e "You chose to go home."
    e "Hai scelto di andare a casa."

# game/tutorial_screen_displayables.rpy:686
translate italian imagemap_done_48eca0a4:

    # e "Anyway..."
    e "Comunque..."

# game/tutorial_screen_displayables.rpy:691
translate italian imagemap_done_a60635a1:

    # e "To demonstrate how imagemaps are put together, I'll show you the five images that make up a smaller imagemap."
    e "Per dimostrare come le imagemap sono messe insieme, ti mostrerò le cinque immagini che compongono una imagemap più piccola."

# game/tutorial_screen_displayables.rpy:697
translate italian imagemap_done_ac9631ef:

    # e "The idle image is used for the background of the imagemap, for hotspot buttons that aren't focused or selected, and for the empty part of an unfocused bar."
    e "L'immagine idle viene usata per lo sfondo dell'imagemap, per i pulsanti hotspot che non sono focalizzati o selezionati, e per la parte vuota di una barra non focalizzata."

# game/tutorial_screen_displayables.rpy:703
translate italian imagemap_done_123b5924:

    # e "The hover image is used for hotspots that are focused but not selected, and for the empty part of a focused bar."
    e "L'immagine hover viene usata per gli hotspot che sono focalizzati ma non selezionati, e per la parte vuota di una barra focalizzata."

# game/tutorial_screen_displayables.rpy:705
translate italian imagemap_done_37f538dc:

    # e "Notice how both the bar and button are highlighted in this image. When we display them as part of a screen, only one of them will show up as focused."
    e "Nota come sia la barra che il pulsante sono evidenziati in questa immagine. Quando li visualizziamo come parte di uno screen, solo uno di essi apparirà come focalizzato."

# game/tutorial_screen_displayables.rpy:711
translate italian imagemap_done_c76b072d:

    # e "Selected images like this selected_idle image are used for parts of the bar that are filled, and for selected buttons, like the current screen and a checked checkbox."
    e "Le immagini selected come questa immagine selected_idle vengono usate per parti della barra che sono piene e per pulsanti selezionati, come lo screen corrente e una casella di controllo selezionata."

# game/tutorial_screen_displayables.rpy:717
translate italian imagemap_done_241a4112:

    # e "Here's the selected_hover image. The button here will never be shown, since it will never be marked as selected."
    e "Ecco l'immagine selected_hover. Il pulsante qui non verrà mai mostrato, poiché non verrà mai contrassegnato come selezionato."

# game/tutorial_screen_displayables.rpy:723
translate italian imagemap_done_3d8f454c:

    # e "Finally, an insensitive image can be given, which is used when a hotspot can't be interacted with."
    e "Infine, può essere fornita un'immagine insensitive, che viene usata quando un hotspot non può essere interagito."

# game/tutorial_screen_displayables.rpy:728
translate italian imagemap_done_ca286729:

    # e "Imagemaps aren't limited to just images. Any displayable can be used where an image is expected."
    e "Le imagemap non sono limitate solo alle immagini. Qualsiasi displayable può essere usato dove è prevista un'immagine."

# game/tutorial_screen_displayables.rpy:743
translate italian imagemap_done_6060b17f:

    # e "Here's an imagemap built using those five images. Now that it's an imagemap, you can interact with it if you want to."
    e "Ecco un'imagemap costruita usando quelle cinque immagini. Ora che è un'imagemap, puoi interagire con essa se vuoi."

# game/tutorial_screen_displayables.rpy:755
translate italian imagemap_done_c817794d:

    # e "To make this a little more concise, we can replace the five images with the auto property, which replaces '%%s' with 'idle', 'hover', 'selected_idle', 'selected_hover', or 'insensitive' as appropriate."
    e "Per renderlo un po' più conciso, possiamo sostituire le cinque immagini con la proprietà auto, che sostituisce '%%s' con 'idle', 'hover', 'selected_idle', 'selected_hover' o 'insensitive' come appropriato."

# game/tutorial_screen_displayables.rpy:757
translate italian imagemap_done_c1ed91b8:

    # e "Feel free to omit the selected and insensitive images if your game doesn't need them. Ren'Py will use the idle or hover images to replace them."
    e "Sentiti libero di omettere le immagini selected e insensitive se il tuo gioco non ne ha bisogno. Ren'Py userà le immagini idle o hover per sostituirle."

# game/tutorial_screen_displayables.rpy:759
translate italian imagemap_done_166f75db:

    # e "The hotspot and hotbar statements describe areas of the imagemap that should act as buttons or bars, respectively."
    e "Le istruzioni hotspot e hotbar descrivono aree dell'imagemap che dovrebbero agire come pulsanti o barre, rispettivamente."

# game/tutorial_screen_displayables.rpy:761
translate italian imagemap_done_becb9688:

    # e "Both take the coordinates of the area, in (x, y, width, height) format."
    e "Entrambe prendono le coordinate dell'area, nel formato (x, y, larghezza, altezza)."

# game/tutorial_screen_displayables.rpy:763
translate italian imagemap_done_fd56baa2:

    # e "A hotspot takes an action that is run when the hotspot is activated. It can also take actions that are run when it's hovered and unhovered, just like a button can."
    e "Un hotspot prende un'azione che viene eseguita quando l'hotspot viene attivato. Può anche prendere azioni che vengono eseguite quando viene evidenziato e de-evidenziato, proprio come può fare un pulsante."

# game/tutorial_screen_displayables.rpy:765
translate italian imagemap_done_5660a6a2:

    # e "A hotbar takes a BarValue object that describes how full the bar is, and the range of values the bar should display, just like a bar and vbar does."
    e "Un hotbar prende un oggetto BarValue che descrive quanto è piena la barra e l'intervallo di valori che la barra dovrebbe visualizzare, proprio come fanno bar e vbar."

# game/tutorial_screen_displayables.rpy:772
translate italian imagemap_done_10496a29:

    # e "A useful pattern is to define a screen with an imagemap that has hotspots that jump to labels, and call that using the call screen statement."
    e "Un pattern utile è definire uno screen con un'imagemap che ha hotspot che saltano a etichette, e chiamarlo usando l'istruzione call screen."

# game/tutorial_screen_displayables.rpy:774
translate italian imagemap_done_dcb45224:

    # e "That's what we did in the school example I showed before. Here's the script for it. It's long, but the imagemap itself is fairly simple."
    e "È quello che abbiamo fatto nell'esempio della scuola che ho mostrato prima. Ecco lo script per esso. È lungo, ma l'imagemap stessa è abbastanza semplice."

# game/tutorial_screen_displayables.rpy:778
translate italian imagemap_done_5b5bc5e5:

    # e "Imagemaps have pluses and minuses. On one hand, they are easy for a designer to create, and can look very good. At the same time, they can be hard to translate, and text baked into images may be blurry when the window is scaled."
    e "Le imagemap hanno pro e contro. Da un lato, sono facili da creare per un designer e possono avere un aspetto molto buono. Allo stesso tempo, possono essere difficili da tradurre e il testo incorporato nelle immagini può essere sfocato quando la finestra viene ridimensionata."

# game/tutorial_screen_displayables.rpy:780
translate italian imagemap_done_b6cebf2b:

    # e "It's up to you and your team to decide if imagemaps are right for your project."
    e "Sta a te e al tuo team decidere se le imagemap sono giuste per il tuo progetto."

# game/tutorial_screen_displayables.rpy:787
translate italian viewport_displayables_e509d50d:

    # e "Sometimes, you'll want to display something bigger than the screen. That's what the viewport displayable is for."
    e "A volte vorrai visualizzare qualcosa di più grande dello schermo. È per questo che esiste il displayable viewport."

# game/tutorial_screen_displayables.rpy:803
translate italian viewport_displayables_9853b0e3:

    # e "Here's an example of a simple viewport, used to display a single image that's far bigger than the screen. Since the viewport will expand to the size of the screen, we use the xysize property to make it smaller."
    e "Ecco un esempio di un viewport semplice, usato per visualizzare una singola immagine che è molto più grande dello schermo. Poiché il viewport si espanderà alle dimensioni dello schermo, usiamo la proprietà xysize per renderlo più piccolo."

# game/tutorial_screen_displayables.rpy:805
translate italian viewport_displayables_778668c8:

    # e "By default the viewport can't be moved, so we give the draggable, mousewheel, and arrowkeys properties to allow it to be moved in multiple ways."
    e "Per impostazione predefinita il viewport non può essere spostato, quindi diamo le proprietà draggable, mousewheel e arrowkeys per permettere di spostarlo in più modi."

# game/tutorial_screen_displayables.rpy:820
translate italian viewport_displayables_bbd63377:

    # e "When I give the viewport the edgescroll property, the viewport automatically scrolls when the mouse is near its edges. The two numbers are the size of the edges, and the speed in pixels per second."
    e "Quando do al viewport la proprietà edgescroll, il viewport scorre automaticamente quando il mouse è vicino ai suoi bordi. I due numeri sono la dimensione dei bordi e la velocità in pixel al secondo."

# game/tutorial_screen_displayables.rpy:839
translate italian viewport_displayables_7c4678ee:

    # e "Giving the viewport the scrollbars property surrounds it with scrollbars. The scrollbars property can take 'both', 'horizontal', and 'vertical' as values."
    e "Dare al viewport la proprietà scrollbars lo circonda con barre di scorrimento. La proprietà scrollbars può prendere 'both', 'horizontal' e 'vertical' come valori."

# game/tutorial_screen_displayables.rpy:841
translate italian viewport_displayables_197953b5:

    # e "The spacing property controls the space between the viewport and its scrollbars, in pixels."
    e "La proprietà spacing controlla lo spazio tra il viewport e le sue barre di scorrimento, in pixel."

# game/tutorial_screen_displayables.rpy:864
translate italian viewport_displayables_54dd6e7b:

    # e "The xinitial and yinitial properties set the initial amount of scrolling, as a fraction of the amount that can be scrolled."
    e "Le proprietà xinitial e yinitial impostano la quantità iniziale di scorrimento, come frazione della quantità che può essere scorsa."

# game/tutorial_screen_displayables.rpy:890
translate italian viewport_displayables_ae4ff821:

    # e "Finally, there's the vpgrid displayable. It combines a viewport and a grid into a single displayable, except it's more efficient than either, since it doesn't have to draw every child."
    e "Infine, c'è il displayable vpgrid. Combina un viewport e una griglia in un singolo displayable, tranne che è più efficiente di entrambi, poiché non deve disegnare ogni figlio."

# game/tutorial_screen_displayables.rpy:892
translate italian viewport_displayables_71fa0b8f:

    # e "It takes the cols and rows properties, which give the number of rows and columns of children. If one is omitted, Ren'Py figures it out from the other and the number of children."
    e "Prende le proprietà cols e rows, che danno il numero di righe e colonne di figli. Se una viene omessa, Ren'Py la deduce dall'altra e dal numero di figli."

translate italian strings:

    # game/tutorial_screen_displayables.rpy:9
    old "Common properties all displayables share."
    new "Proprietà comuni che tutti i displayable condividono."

    # game/tutorial_screen_displayables.rpy:9
    old "Adding images and other displayables."
    new "Aggiungere immagini e altri displayable."

    # game/tutorial_screen_displayables.rpy:9
    old "Text."
    new "Testo."

    # game/tutorial_screen_displayables.rpy:9
    old "Boxes and other layouts."
    new "Scatole e altri layout."

    # game/tutorial_screen_displayables.rpy:9
    old "Windows and frames."
    new "Finestre e frame."

    # game/tutorial_screen_displayables.rpy:9
    old "Buttons."
    new "Pulsanti."

    # game/tutorial_screen_displayables.rpy:9
    old "Bars."
    new "Barre."

    # game/tutorial_screen_displayables.rpy:9
    old "Viewports."
    new "Viewport."

    # game/tutorial_screen_displayables.rpy:9
    old "Imagemaps."
    new "Imagemap."

    # game/tutorial_screen_displayables.rpy:9
    old "That's all for now."
    new "È tutto per ora."

    # game/tutorial_screen_displayables.rpy:55
    old "This uses position properties."
    new "Questo usa proprietà di posizione."

    # game/tutorial_screen_displayables.rpy:63
    old "And the world turned upside down..."
    new "E il mondo si capovolse..."

    # game/tutorial_screen_displayables.rpy:115
    old "Flight pressure in tanks."
    new "Pressione di volo nei serbatoi."

    # game/tutorial_screen_displayables.rpy:116
    old "On internal power."
    new "Su alimentazione interna."

    # game/tutorial_screen_displayables.rpy:117
    old "Launch enabled."
    new "Lancio abilitato."

    # game/tutorial_screen_displayables.rpy:118
    old "Liftoff!"
    new "Decollo!"

    # game/tutorial_screen_displayables.rpy:232
    old "The answer is [answer]."
    new "La risposta è [answer]."

    # game/tutorial_screen_displayables.rpy:244
    old "Text tags {color=#c8ffc8}work{/color} in screens."
    new "I tag di testo {color=#c8ffc8}funzionano{/color} negli screen."

    # game/tutorial_screen_displayables.rpy:336
    old "Bigger"
    new "Più grande"

    # game/tutorial_screen_displayables.rpy:401
    old "This is a screen."
    new "Questo è uno screen."

    # game/tutorial_screen_displayables.rpy:402
    old "Okay"
    new "Okay"

    # game/tutorial_screen_displayables.rpy:440
    old "You clicked the button."
    new "Hai cliccato il pulsante."

    # game/tutorial_screen_displayables.rpy:441
    old "Click me."
    new "Cliccami."

    # game/tutorial_screen_displayables.rpy:453
    old "You hovered the button."
    new "Hai evidenziato il pulsante."

    # game/tutorial_screen_displayables.rpy:454
    old "You unhovered the button."
    new "Hai de-evidenziato il pulsante."

    # game/tutorial_screen_displayables.rpy:470
    old "Heal"
    new "Cura"

    # game/tutorial_screen_displayables.rpy:479
    old "This is a textbutton."
    new "Questo è un textbutton."

    # game/tutorial_screen_displayables.rpy:539
    old "Or me."
    new "O me."

    # game/tutorial_screen_displayables.rpy:541
    old "You clicked the other button."
    new "Hai cliccato l'altro pulsante."

