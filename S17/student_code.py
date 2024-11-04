def validate(data, template):
    """
    Validates a dictionary against a template structure.
    
    Args:
        data (dict): Dictionary to validate
        template (dict): Template dictionary defining the expected structure
    
    Returns:
        tuple: (bool, str) - (True, '') if valid, (False, error_message) if invalid
    """
    def _validate_recursive(d, t, current_path=''):
        # Check template keys in order they appear
        for key in t.keys():
            if key not in d:
                path = f"{current_path}{key}" if not current_path else f"{current_path}.{key}"
                return False, f"mismatched keys: {path}"
        
        # Check for extra keys in data in order they appear
        for key in d.keys():
            if key not in t:
                path = f"{current_path}{key}" if not current_path else f"{current_path}.{key}"
                return False, f"mismatched keys: {path}"
        
        # Check each key-value pair in template order
        for key, expected_type in t.items():
            path = f"{current_path}{key}" if not current_path else f"{current_path}.{key}"
            value = d[key]
            
            if isinstance(expected_type, dict):
                if not isinstance(value, dict):
                    return False, f"bad type: {path}"
                
                # Recursive validation
                state, error = _validate_recursive(value, expected_type, path + '.')
                if not state:
                    return False, error
            else:
                if not isinstance(value, expected_type):
                    return False, f"bad type: {path}"
        
        return True, ''
    
    # Start validation from the top level
    return _validate_recursive(data, template) 