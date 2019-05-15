from blog_client import BlogClient

def main():
    val = 'RUN'

    while val:
        print("What would you like to do next?")
        val = input('[w]rite a post or [r]ead them?')

        if val == 'w':
            write_post()
        elif val == 'r':
            read_posts()
        
def read_posts():
    svc = BlogClient()
    response = svc.all_entries()
    response.raise_for_status()

    posts = response.json()
    for idx, p in enumerate(posts, 1):
        print("{}. [{} views] {}".format(
            idx,
            p.get('view_count'), 
            p.get('title')
        ))
    print()
    selected = int(input('Which number to view? '))
    
    selected_id = posts[selected-1].get('id')
    
    response = svc.entry_by_id(selected_id)
    response.raise_for_status()

    selected_post = response.json()
    print("Details for selected post: {}".format(selected_post.get('id')))
    print("Title: " + selected_post.get('title'))
    print("Written: " + selected_post.get('published'))
    print("Content: " + selected_post.get('content'))
    print()
    print()


    #print(selected_id)
    #print(type(response), response)

def write_post():
    pass

if __name__ == "__main__":
    main()
