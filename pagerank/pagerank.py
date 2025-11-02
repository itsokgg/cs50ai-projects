import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    if page not in corpus:
        return dict()
    # get the links on the page
    links = corpus.get(page)
    prob_dist = dict()
    # initialize len of corpus so that program wont have to calculate it multiple times
    len_corpus = len(corpus)

    if len(links) > 0:
        # for every link on the page add it to prob_dist with its proportional probability
        for link in links:
            page_prob = damping_factor / len(links)
            prob_dist[link] = page_prob
    
        # add probability for all pages if surfer randomly chooses a link in the corpus
        for p in corpus:
            rand_prob = (1 - damping_factor) / len_corpus
            if p in prob_dist:
                prob_dist[p] += rand_prob
            else:
                prob_dist[p] = rand_prob
    # if no links on page
    else:
        for p in corpus:
            rand_prob = 1 / len_corpus
            prob_dist[p] = rand_prob

    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # first sample
    sample = random.choice(list(corpus))
    page_rank = {page: float(0) for page in corpus}

    for _ in range(n):
        tm = transition_model(corpus, sample, damping_factor)
        sample = random.choices(list(tm), weights=tm.values())[0]
        page_rank[sample] += (1 / n)

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # initialize new_corpus and set values of all pages without links to all the pages in corpus
    new_corpus = dict()
    pages = {page for page in corpus}
    for page in corpus:
        if len(corpus[page]) == 0:
            new_corpus[page] = pages
        else:
            new_corpus[page] = corpus[page]

    # initialize len of corpus so that program wont have to calculate it multiple times
    len_corpus = len(new_corpus)
    # set initial page rank
    page_ranks = {page: 1 / len_corpus for page in new_corpus}
    # keep track of iterations with change of less than 0.001
    iterations = 0
    
    while iterations != len_corpus:
        # reset iterations everytime while loop runs
        iterations = 0
        for page in page_ranks:
            # get all the pages that link to this page
            new_page_rank = 0
            for i in new_corpus:
                if page in new_corpus[i]:
                    # add the rank of i as the key and number of links in i as value
                    new_page_rank += page_ranks[i] / len(new_corpus[i])

            # multiply new_page_rank by damping_factor
            new_page_rank *= damping_factor

            # add probability for if surfer chose a page to new_page_rank
            new_page_rank += (1 - damping_factor) / len_corpus
            
            # check if new_page_rank didnt change much from the old one:
            if abs(page_ranks[page] - new_page_rank) <= 0.001:
                iterations += 1
            
            page_ranks[page] = new_page_rank

    return page_ranks

            

if __name__ == "__main__":
    main()
