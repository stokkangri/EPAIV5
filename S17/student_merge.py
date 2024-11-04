from collections import defaultdict, Counter

def merge_with_defaultdict(*dicts):
    """
    Merges multiple dictionaries of word frequencies using defaultdict.
    Returns the merged dictionary sorted by frequency in descending order.
    
    Args:
        *dicts: Variable number of dictionaries with word frequencies
        
    Returns:
        dict: Merged dictionary sorted by frequency in descending order
    """
    # Initialize defaultdict with int as default factory
    merged = defaultdict(int)
    
    # Add frequencies from all dictionaries
    for d in dicts:
        for word, freq in d.items():
            merged[word] += freq
    
    # Convert to regular dict and sort by frequency
    # If frequencies are equal, sort by word alphabetically
    sorted_items = sorted(merged.items(), key=lambda x: (-x[1], x[0]))
    return dict(sorted_items)

def merge_with_counter(*dicts):
    """
    Merges multiple dictionaries of word frequencies using Counter.
    Returns the merged dictionary sorted by frequency in descending order.
    
    Args:
        *dicts: Variable number of dictionaries with word frequencies
        
    Returns:
        dict: Merged dictionary sorted by frequency in descending order
    """
    # Initialize empty Counter
    merged = Counter()
    
    # Add all dictionaries to the Counter
    for d in dicts:
        merged.update(d)
    
    # Sort by frequency and convert to regular dict
    # If frequencies are equal, sort by word alphabetically
    sorted_items = sorted(merged.items(), key=lambda x: (-x[1], x[0]))
    return dict(sorted_items) 