import c

# Find the position of the first crash.

(tracks, carts) = c.parseTrackFile("i1.txt")

while True:
	for cart in carts:
		current_seg = tracks[cart.seg.y][cart.seg.x]
		next_seg = c.getNextTrackSegment(tracks, cart)

		# The first cart crash.
		if next_seg.cart is not None:
			print(str(next_seg.x) + "," + str(next_seg.y))
			exit()

		cart.moveTo(next_seg)
