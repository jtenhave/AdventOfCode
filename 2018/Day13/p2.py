import c

# Find the position of the last cart that did not crash.

(tracks, carts) = c.parseTrackFile("i1.txt")

while True:

	if len(carts) == 1:
		print(str(carts[0].seg.x) + "," + str(carts[0].seg.y))
		exit()

	crashed = set()

	for cart in carts:

		if cart in crashed:
			continue

		current_seg = tracks[cart.seg.y][cart.seg.x]
		next_seg = c.getNextTrackSegment(tracks,cart)

		# Remove carts that crashed.
		if next_seg.cart is not None:
			crashed |= { next_seg.cart, cart }
			next_seg.cart = None
			cart.seg.cart = None

		else:
			cart.moveTo(next_seg)

	for cart in crashed:
		carts.remove(cart)

	carts.sort(key=lambda c: (c.seg.y, cart.seg.x))
		