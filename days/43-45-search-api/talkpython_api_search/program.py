import api
import webbrowser


def main():
    print("******* SEARCH TALK PYTHON *******")
    keyword = input('Keyword to search: ')
    results = api.find_items_by_keyword(keyword)

    if(len(results) > 0):
        print(f'There are {len(results)} matching episodes:')
        iCounter = 1
        for r in results:
            print(f"{str(iCounter)}. {r.title}")
            iCounter += 1

        print()
        episodeNum = input("Enter the number of the episode to view: ")
        episodeIndex = int(episodeNum) - 1  # number is 1-based
        episodeUrl = results[episodeIndex].url
        episodeTitle = results[episodeIndex].title
        fullUrl = f'https://talkpython.fm{episodeUrl}'

        print(f"Opening link for #{episodeNum} ({episodeTitle}) in browser...")
        webbrowser.open(fullUrl, new=2)
        print("Done")

    else:
        print(f'There are no matching episodes.')

if __name__ == '__main__':
    main()
