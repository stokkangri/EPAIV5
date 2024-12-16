def validate(data, template):
    """
    Validates a dictionary against a template structure.
    
    Args:
        data (dict): Dictionary to validate
        template (dict): Template dictionary defining the expected structure
    
    Returns:
        tuple: (bool, str) - (True, '') if valid, (False, error_message) if invalid
               Error message includes the exact path where validation failed
    """
    def check_structure(data_part, template_part, path=""):
        # Check if data_part and template_part have the same keys
        data_keys = set(data_part.keys())
        template_keys = set(template_part.keys())
        
        # Check for missing keys first, in template order
        for key in template_part:
            if key not in data_keys:
                full_path = f"{path}.{key}" if path else key
                return False, f"mismatched keys: {full_path}"
        
        # Then check for extra keys
        for key in sorted(data_keys - template_keys):
            full_path = f"{path}.{key}" if path else key
            return False, f"mismatched keys: {full_path}"
        
        # Check each key-value pair against the template
        for key in template_part:
            # Build the path for the current key
            current_path = key if not path else f"{path}.{key}"
            
            # None values are considered invalid for any type
            if data_part[key] is None:
                return False, f"bad type: {current_path}"
            
            # Handle both primitive types and nested dictionaries
            if isinstance(template_part[key], type):
                if not isinstance(data_part[key], template_part[key]):
                    return False, f"bad type: {current_path}"
            elif isinstance(template_part[key], dict):
                if not isinstance(data_part[key], dict):
                    return False, f"bad type: {current_path}"
                valid, error = check_structure(data_part[key], template_part[key], current_path)
                if not valid:
                    return False, error
                    
        return True, ""

    return check_structure(data, template) 