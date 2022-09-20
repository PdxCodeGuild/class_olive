from flask import Flask, render_template

app = Flask(__name__)

post_one_fstr = f'''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce a congue sem. Pellentesque id enim commodo, gravida risus eget, tempor lectus. Praesent laoreet nisi non dui faucibus sollicitudin. Nulla porta neque eget velit placerat pretium. Vivamus sit amet justo fermentum, porttitor est in, tempus nunc. Integer congue diam eu ante aliquet ornare. In hac habitasse platea dictumst.

        Nulla gravida et ante non tempor. Fusce vestibulum, nisl iaculis venenatis viverra, nunc metus feugiat purus, id dictum augue orci et ipsum. Integer magna libero, fringilla id mattis efficitur, volutpat a dolor. Nunc sed elementum metus, eget commodo tortor. Donec dapibus ipsum turpis, sed aliquet massa mattis ut. Cras pretium, leo ac auctor venenatis, diam elit lacinia libero, sed porta augue nunc placerat mauris. Praesent a massa facilisis, volutpat diam non, fermentum nunc. Integer eu eros in magna consectetur varius nec nec nulla.
         
        Praesent eget arcu lorem. In hac habitasse platea dictumst. Nullam volutpat interdum metus sit amet placerat. Cras porta dui sit amet orci blandit tristique. Ut maximus pretium posuere. Proin id porta tortor. Proin gravida ante vel odio viverra placerat. Nunc lobortis pulvinar arcu a blandit. Vestibulum non arcu eget dolor ultricies condimentum id eget arcu. Curabitur cursus nunc eget nibh porta aliquam. Nulla ac venenatis felis. Vivamus volutpat nulla molestie augue condimentum cursus. Pellentesque vestibulum placerat libero. Praesent mauris odio, ullamcorper id fringilla vel, suscipit sed risus. Sed pellentesque velit et vulputate ornare. Donec sit amet ex eu magna venenatis semper.'''


blog_post_1 = {
    'title': 'The Problem with Doors',
    'author': 'Bob Dooglehousette',
    'date': '9/19/2022',
    'body': post_one_fstr
}


post_two_fstr=f'''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eleifend luctus erat, eget finibus nisi faucibus vel. Donec pulvinar fermentum metus, vitae scelerisque nisl egestas eget. In in molestie mauris. Nam nec pharetra ante. Vivamus vel lectus eu velit ultrices auctor nec ut metus. Nam tempor, leo in sodales malesuada, mauris ante vestibulum nisl, commodo bibendum urna metus vitae lorem. Ut interdum mi metus, ac dignissim diam pretium sed. Nam vulputate ipsum nec elit tempus euismod. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Maecenas dui quam, consectetur fermentum tristique non, sollicitudin sit amet lacus.
        
        Proin laoreet tellus non urna euismod, eget suscipit magna lobortis. Nullam eget nulla et lacus posuere imperdiet. Curabitur metus nulla, ullamcorper non viverra ut, vehicula ac velit. Nam fringilla tempor lacus, varius blandit arcu fringilla non. Mauris placerat ullamcorper tellus venenatis faucibus. Curabitur commodo eros magna. Sed id elit odio. Duis eget elementum nisi. Ut in porttitor est. Nunc porta lacinia sollicitudin. Sed ornare euismod enim, in imperdiet magna finibus et. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas rhoncus convallis tincidunt.
        
        Ut quis tortor lorem. Aliquam molestie condimentum luctus. Sed iaculis velit sit amet nisl vestibulum dignissim. Duis sollicitudin tortor quis enim hendrerit bibendum. Aenean vel dolor vehicula, suscipit purus vel, posuere erat. Nunc sollicitudin, odio posuere ultricies facilisis, mi nisl efficitur ligula, vel pellentesque dolor tortor quis risus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec ut vulputate sapien, eget faucibus lectus. Donec malesuada sem ac lectus malesuada pharetra. Nulla vulputate ullamcorper quam non tincidunt. Aliquam porttitor, nisl eu feugiat accumsan, neque sem aliquam nunc, eget suscipit purus augue at nulla. Aliquam purus ipsum, vestibulum eu porttitor ut, euismod vitae nunc. Morbi sapien libero, posuere sit amet sollicitudin id, maximus ut turpis. Praesent nec massa ipsum. In et orci mauris.'''


blog_post_2 = {
    'title': "The Queen Isn't real?",
    'author': 'Tara Boutique',
    'date': '9/12/2022',
    'body': post_two_fstr
}

post_three_fstr=f'''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tincidunt egestas semper. Curabitur congue condimentum massa in elementum. Integer ex nibh, elementum laoreet dignissim sed, varius et ante. Etiam laoreet id lorem ac viverra. Pellentesque cursus, quam vel gravida suscipit, elit mauris iaculis lorem, sit amet ultricies nulla orci a tellus. Nam in ipsum tortor. Nunc sit amet accumsan nisl. Aliquam porttitor ullamcorper erat lacinia sodales. Fusce nec iaculis enim. Aenean id mi nec neque fringilla scelerisque at iaculis libero. Sed consectetur dolor ac risus consequat dapibus vel et metus. Mauris eget diam sem. Nullam venenatis elementum leo, et mattis purus congue vitae. Praesent laoreet faucibus lectus.
        
        Sed scelerisque, ante nec consectetur lacinia, massa eros ultricies tellus, in eleifend lectus sapien eget velit. In aliquam, lacus non ornare consectetur, tortor turpis iaculis magna, congue porta odio dolor quis purus. Vivamus fringilla sem eget iaculis volutpat. Morbi feugiat id dui non aliquet. Pellentesque consectetur, quam eu placerat aliquam, lorem nisi porttitor mi, vitae ullamcorper lorem tortor eu felis. Nullam egestas sollicitudin nisi, sit amet feugiat justo finibus quis. Donec erat elit, accumsan ut aliquet sit amet, convallis ut diam. Phasellus id tellus in neque consequat condimentum at sit amet magna. Aenean euismod libero diam, sed accumsan neque varius quis. Suspendisse at metus pharetra, elementum risus ac, placerat nibh.
        
        Donec lobortis dignissim malesuada. Curabitur tristique gravida suscipit. Vivamus convallis ligula vitae velit aliquet elementum. In non pellentesque enim. Nunc porttitor felis at luctus malesuada. Nunc sagittis nibh eget massa imperdiet congue. Nulla eu aliquet lacus. Aenean eget euismod nunc. Sed quis nisi laoreet, pellentesque justo quis, faucibus lectus. Aenean tempor eros sed quam aliquam, et tincidunt leo tempor. Donec auctor fringilla metus, eu lacinia lacus sodales eget. Ut accumsan fringilla tortor. Aliquam scelerisque felis risus, sit amet mollis elit facilisis vitae. Ut purus quam, hendrerit quis sapien id, accumsan consequat libero. Pellentesque vitae ante nibh.
        
        Pellentesque metus eros, facilisis quis ullamcorper et, lacinia quis mi. Integer lorem sapien, ornare eu commodo eu, sagittis eget metus. Vestibulum quis nisl convallis, pulvinar dui porttitor, tempus est. Maecenas posuere purus eu velit ultrices, at semper magna consectetur. Donec imperdiet gravida feugiat. Praesent cursus mauris eu elit aliquet, pretium rutrum tellus lacinia. Phasellus eu elit in leo commodo commodo vel non nulla. Donec fermentum enim arcu, non sagittis nunc elementum eget.'''


blog_post_3 = {
    'title': 'Unstoppable Train Stops',
    'author': 'Tom Bombadil',
    'date': '9/2/2022',
    'body': post_three_fstr
}


post_four_fstr=f'''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam finibus augue magna, non convallis mauris semper nec. Mauris eu feugiat ipsum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus cursus odio at urna rhoncus, vel bibendum eros tincidunt. Pellentesque quis lorem pretium nibh pharetra ornare a sed urna. Nunc rutrum, lacus sed placerat feugiat, quam ante commodo mi, sit amet cursus diam lacus non urna. Nullam quis dolor maximus, bibendum felis sit amet, lacinia quam. Aenean ut metus at odio ultricies vulputate et non elit. Vestibulum vitae ligula dignissim, venenatis nunc sit amet, ultrices nulla. Vivamus ultricies arcu ut nunc accumsan, id vestibulum sapien sodales. Morbi id ante ac turpis molestie ultrices. Nam ut volutpat nisl. Integer massa massa, venenatis ut lacinia vel, mollis ac lectus. Mauris ut fermentum tellus. Proin fermentum enim sed pharetra mollis. Proin tincidunt mattis fringilla.
        
        Vestibulum sem purus, ullamcorper eget cursus in, sagittis rutrum enim. Phasellus eu sagittis ipsum, quis gravida orci. Aenean bibendum non eros non elementum. Integer sit amet facilisis dolor, scelerisque efficitur dui. Integer in nulla eget urna ornare vestibulum et ac lacus. Nam viverra odio sit amet viverra iaculis. Nulla elementum sed mi quis ultrices. Aliquam sed ex eget eros lacinia fringilla in nec leo. Nam ornare enim et ullamcorper pellentesque. Nam rhoncus ultricies pellentesque.
        
        Praesent mollis sem non justo iaculis volutpat. Pellentesque et faucibus metus. Nam vulputate ullamcorper tempus. Nunc ultrices mi at nisl tempor molestie. Praesent quis augue eget urna cursus vestibulum. Donec quis porta purus, sed facilisis purus. Proin viverra nibh quis ultricies faucibus. Mauris ut massa rhoncus, euismod tellus ut, convallis dui.
        
        Phasellus sit amet magna eu massa ornare facilisis et ac velit. Nam dapibus nunc ut porta ornare. Suspendisse nec nisl sit amet ex maximus lobortis nec a nunc. Quisque ut laoreet nibh. Maecenas ullamcorper dui nunc, sit amet accumsan justo congue pellentesque. Pellentesque metus massa, consequat non convallis non, aliquam quis nisl. In convallis scelerisque lectus, vitae lobortis magna sodales ac.
        
        Cras elementum mollis libero, non congue mi consectetur et. Fusce mi ligula, dictum ac erat sed, ultrices malesuada urna. Duis id dapibus eros. Donec scelerisque fringilla sem, vitae commodo est placerat id. Vestibulum eget mauris condimentum, eleifend massa imperdiet, cursus nunc. Nullam molestie vestibulum nunc tincidunt blandit. Ut euismod accumsan est, in posuere urna aliquet et.'''



blog_post_4 = {
    'title': "What I'm Wearing",
    'author': "Ebony Dark'ness Dementia Raven Way",
    'date': '8/29/2006',
    'body': post_four_fstr
}


@app.route('/')
def home():
    return render_template('index.html', blog_post_1=blog_post_1, blog_post_2=blog_post_2, blog_post_3=blog_post_3, blog_post_4=blog_post_4)


@app.route('/about/')
def about():
    return render_template('index_about.html', blog_post_1=blog_post_1)