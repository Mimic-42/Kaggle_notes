flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers))
print(flowers)

# ----------------------------------------------------------

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)

# -----------------------------------------------------------

# The list has ten entries
print(len(flowers_list))

# -----------------------------------------------------------

print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])

# ------------------------------------------------------------

# Slicing
print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

# ------------------------------------------------------------

# Removing items
flowers_list.remove("globe thistle")
print(flowers_list)

# ------------------------------------------------------------

# adding items
flowers_list.append("snapdragon")
print(flowers_list)

