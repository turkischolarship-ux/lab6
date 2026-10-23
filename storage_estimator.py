# Storage Estimator Script

mb_size = float(input("Enter size in MB: "))

# Conversion to GB
gb_size = mb_size / 1024

print(f"Size in MB: {mb_size} MB")
print(f"Size in GB: {gb_size:.2f} GB")