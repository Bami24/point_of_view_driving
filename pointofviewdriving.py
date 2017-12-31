import car
import motorbike
import fresh_tomatoes

# Please note '# noqa' comments are include for the URL exception to PEP8

# Below are instances of Car, which takes a make, model, model image(url)
# point of view video(youtube url) and a right hand drive point of
# view video (youtube url).

ford_fiesta = car.Car("Ford",
                      "Fiesta",
                      "https://www.fordeumedia-e.ford.com/nas/gforcenaslive/gbr/00m/yyj/images/gbr00myyjjd3jed(a)(a)jknshowroom_0_0.png",  # noqa
                      "https://www.youtube.com/watch?v=iDTG8AevN54",
                      "https://www.youtube.com/watch?v=yCUX4AtlyLA")

ford_focus = car.Car("Ford", "Focus",
                     "https://www.fordeumedia-b.ford.com/nas/gforcenaslive/gbr/00l/yyh/images/gbr00lyyh1j52lp(a)(a)cozshowroom_0_0.png",  # noqa
                     "https://www.youtube.com/watch?v=6nBLEmkZgO0",
                     "https://www.youtube.com/watch?v=yYkA1-LIGQg")

ford_kaplus = car.Car("Ford", "KA+",
                     "https://www.fordeumedia-b.ford.com/nas/gforcenaslive/gbr/001/yyj/images/gbr001yyjelvepa(a)(a)h8eshowroom_0_0.png",  # noqa
                     "https://www.youtube.com/watch?v=6-5i_A0Dpwk",
                     "https://www.youtube.com/watch?v=yMf9fZMyDL4")

ford_focusrs = car.Car("Ford", "FocusRS",
                     "https://www.fordeumedia-d.ford.com/nas/gforcenaslive/gbr/00l/yyh/images/gbr00lyyh1j51tt(a)(a)co3showroom_0_0.png",  # noqa
                     "https://www.youtube.com/watch?v=7nppW37J4_Q",
                     "https://www.youtube.com/watch?v=6VFR12LWIVg")

ford_mustang = car.Car("Ford", "Mustang",
                     "https://www.fordeumedia-a.ford.com/nas/gforcenaslive/gbr/00s/yyf/images/gbr00syyfbtmdsb(a)(a)c4fshowroom_0_0.png",  # noqa
                     "https://www.youtube.com/watch?v=rnD0UPpUktE",
                     "https://www.youtube.com/watch?v=-FPgyT5hRZg")

# Below are instances of Motorbike, which takes a make, model, model image(url)
# point of view video(youtube url)

honda_cmx500rebel = motorbike.MotorBike("Honda", "CMX500Rebel",
                                        "http://www.honda.co.uk/content/dam/central/motorcycles/colour-picker/street/cmx500_rebel/cmx500_rebel_nv/nh-b89m_mattearmouredsilvermetallic/nh-b89m_MatteArmouredSilvermetallic.png/_jcr_content/renditions/c1.png",  # noqa
                                        "https://www.youtube.com/watch?v=Gi0tQubQ77k")  # noqa

honda_cb1100ex = motorbike.MotorBike("Honda", "CB1100EX",
                                     "http://www.honda.co.uk/content/dam/central/motorcycles/street/cb1100/2017/CB1100_2017_Studio_Side_1728x972.png/_jcr_content/renditions/c1.png",  # noqa
                                     "https://www.youtube.com/watch?v=7aN4ZDoetuk")  # noqa

honda_cb1100rs = motorbike.MotorBike("Honda", "CB1100RS",
                                     "http://www.honda.co.uk/content/dam/central/motorcycles/colour-picker/street/cb1100_2017/cb1100_2017_rs/nh-b01_graphiteblack/cb1100_rs_nh-b01_GraphiteBlack.png/_jcr_content/renditions/c1.png",  # noqa
                                     "https://www.youtube.com/watch?v=M4MvqWHrVQU")  # noqa

honda_nc750s = motorbike.MotorBike("Honda", "NC750S",
                                   "http://www.honda.co.uk/content/dam/central/motorcycles/street/nc750s/nc750s%202016/nc750s-2016-nav-16x9(1).png/_jcr_content/renditions/c1.png",  # noqa
                                   "https://www.youtube.com/watch?v=ev6gjHCCrRs")  # noqa

honda_cb500f = motorbike.MotorBike("Honda", "CB500F",
                                   "http://www.honda.co.uk/content/dam/central/motorcycles/colour-picker/street/cb500f_2016/cb500f_2016_abs/y-196/CB500F_y-196_LemonIceYellow.png/_jcr_content/renditions/c1.png",  # noqa
                                   "https://www.youtube.com/watch?v=TrPijXtjBAQ")  # noqa

# test units (uncomment to use)
# ford_fiesta.print_details()
# honda_cmx500rebel.print_details()

# below is a array of the car and motorbike
# instances that we created above

vehicle_array = [ford_fiesta, ford_focus, ford_kaplus,
                 ford_focusrs, ford_mustang, honda_cmx500rebel,
                 honda_cb1100ex, honda_cb1100rs, honda_nc750s, honda_cb500f]

# belos is the call to fresh_tomatoes passing in
# the vehicle array
fresh_tomatoes.open_vehicles_page(vehicle_array)
