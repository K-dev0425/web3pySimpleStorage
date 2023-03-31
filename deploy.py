from solcx import compile_standard

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# Compile Our Standard


compiled_sol = compile_standard(
    {
        "languages": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}}
    }
) 