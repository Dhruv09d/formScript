import random
import time

from selenium import webdriver
import names


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("incognito")
# chrome_options.add_argument("--user-data-dir=/home/dhruv/.config/google-chrome")
# chrome_options.add_argument('--profile-directory=Default')
driver = webdriver.Chrome(executable_path='./chromeDriver/chromedriver', options=chrome_options)
url = "https://forms.gle/FDLiNemrC44fEfbS8"
driver.get(url)
time.sleep(2)


def getInputs():
    # input fields
    personName   = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    age    =  driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    weight = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
    height = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
    city   = driver.find_element_by_xpath("//*[@id=\"mG61Hd\"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input")

    # radio buttons
    # gender
    genderFemale = driver.find_element_by_xpath("//*[@id=\"i16\"]")
    genderMale   = driver.find_element_by_xpath("//*[@id=\"i13\"]")
    genderOther  = driver.find_element_by_xpath("//*[@id=\"i19\"]")

    # Occupation
    occupationOfficeJob     = driver.find_element_by_xpath("//*[@id=\"i38\"]")
    occupationFieldJob      = driver.find_element_by_xpath("//*[@id=\"i41\"]")
    occupationBusinessJob   = driver.find_element_by_xpath("//*[@id=\"i44\"]")
    occupationStudentJob    = driver.find_element_by_xpath("//*[@id=\"i47\"]")
    occupationNotWorkingJob = driver.find_element_by_xpath("//*[@id=\"i50\"]")

    # smoke
    smokeDaily           = driver.find_element_by_xpath("//*[@id=\"i57\"]")
    smokeAlternateDays   = driver.find_element_by_xpath("//*[@id=\"i60\"]")
    smokeOnceInWeek      = driver.find_element_by_xpath("//*[@id=\"i63\"]")
    smokeFewTimesInMonth = driver.find_element_by_xpath("//*[@id=\"i66\"]")
    smokeRarely          = driver.find_element_by_xpath("//*[@id=\"i69\"]")
    smokeNever           = driver.find_element_by_xpath("//*[@id=\"i72\"]")


    # alcohol
    alcoholDaily           = driver.find_element_by_xpath("//*[@id=\"i79\"]")
    alcoholAlternateDays   = driver.find_element_by_xpath("//*[@id=\"i82\"]")
    alcoholOnceInWeek      = driver.find_element_by_xpath("//*[@id=\"i85\"]")
    alcoholFewTimesInMonth = driver.find_element_by_xpath("//*[@id=\"i88\"]")
    alcoholRarely          = driver.find_element_by_xpath("//*[@id=\"i91\"]")
    alcoholNever           = driver.find_element_by_xpath("//*[@id=\"i94\"]")


    # meals
    mealInDayOne   = driver.find_element_by_xpath("//*[@id=\"i101\"]")
    mealInDayTwo   = driver.find_element_by_xpath("//*[@id=\"i104\"]")
    mealInDayThree = driver.find_element_by_xpath("//*[@id=\"i107\"]")
    mealInDayFour  = driver.find_element_by_xpath("//*[@id=\"i110\"]")
    mealInDayFive  = driver.find_element_by_xpath("//*[@id=\"i113\"]")


    # junk
    junkDaily           = driver.find_element_by_xpath("//*[@id=\"i120\"]")
    junkAlternateDays   = driver.find_element_by_xpath("//*[@id=\"i123\"]")
    junkOnceInWeek      = driver.find_element_by_xpath("//*[@id=\"i126\"]")
    junkFewTimesInMonth = driver.find_element_by_xpath("//*[@id=\"i129\"]")
    junkRarely          = driver.find_element_by_xpath("//*[@id=\"i132\"]")
    junkNever           = driver.find_element_by_xpath("//*[@id=\"i135\"]")

    #workout
    workoutDaily           = driver.find_element_by_xpath("//*[@id=\"i142\"]")
    workoutAlternateDays   = driver.find_element_by_xpath("//*[@id=\"i145\"]") # //*[@id="i145"]
    workoutOnceInWeek      = driver.find_element_by_xpath("//*[@id=\"i148\"]")
    workoutFewTimesInMonth = driver.find_element_by_xpath("//*[@id=\"i151\"]")
    workoutRarely          = driver.find_element_by_xpath("//*[@id=\"i154\"]")
    workoutNever           = driver.find_element_by_xpath("//*[@id=\"i157\"]") # //*[@id="i154"]

    # type of workout

    workoutTypeGym       = driver.find_element_by_xpath("//*[@id=\"i164\"]")
    workoutTypeRunning   = driver.find_element_by_xpath("//*[@id=\"i167\"]")
    workoutTypeWaling    = driver.find_element_by_xpath("//*[@id=\"i170\"]")
    workoutTypeJogging   = driver.find_element_by_xpath("//*[@id=\"i173\"]")
    workoutTypeCycling   = driver.find_element_by_xpath("//*[@id=\"i176\"]")
    workoutTypeCardio    = driver.find_element_by_xpath("//*[@id=\"i179\"]")
    workoutTypeNoWorkout = driver.find_element_by_xpath("//*[@id=\"i182\"]")

    # eat junk when stressed
    StressEatJunkFoodYes       = driver.find_element_by_xpath("//*[@id=\"i189\"]")
    StressEatJunkFoodSometimes = driver.find_element_by_xpath("//*[@id=\"i192\"]")
    StressEatJunkFoodRarely       = driver.find_element_by_xpath("//*[@id=\"i195\"]")
    StressEatJunkFoodNever       = driver.find_element_by_xpath("//*[@id=\"i198\"]")

    # prefer to eat
    preferJunk            = driver.find_element_by_xpath("//*[@id=\"i205\"]")
    preferHealthy         = driver.find_element_by_xpath("//*[@id=\"i208\"]")
    preferFare            = driver.find_element_by_xpath("//*[@id=\"i211\"]")
    preferNeverConsidered = driver.find_element_by_xpath("//*[@id=\"i214\"]")


    # perticular disease
    diseaseHeart     = driver.find_element_by_xpath("//*[@id=\"i222\"]")
    diseaseAbdomen   = driver.find_element_by_xpath("//*[@id=\"i225\"]") # //*[@id="i225"]
    diseaseAllergies = driver.find_element_by_xpath("//*[@id=\"i228\"]")
    diseaseOther     = driver.find_element_by_xpath("//*[@id=\"i231\"]")

    # metabolism rate
    metabolismFast     = driver.find_element_by_xpath("//*[@id=\"i238\"]")
    metabolismSlow     = driver.find_element_by_xpath("//*[@id=\"i241\"]")
    metabolismModerate = driver.find_element_by_xpath("//*[@id=\"i244\"]")
    metabolismDontKnow = driver.find_element_by_xpath("//*[@id=\"i247\"]")

    # spent on junk food

    spentLot             = driver.find_element_by_xpath("//*[@id=\"i254\"]")
    spentFareAmmount     = driver.find_element_by_xpath("//*[@id=\"i257\"]")
    spentLess            = driver.find_element_by_xpath("//*[@id=\"i260\"]")
    spentNeverConsidered = driver.find_element_by_xpath("//*[@id=\"i263\"]")

    # lifeStyle
    lifestyleHealthy           = driver.find_element_by_xpath("//*[@id=\"i270\"]")
    lifestyleUnhealthy         = driver.find_element_by_xpath("//*[@id=\"i273\"]")
    lifestyleModeratelyHealthy = driver.find_element_by_xpath("//*[@id=\"i276\"]")
    lifestyleCantSay           = driver.find_element_by_xpath("//*[@id=\"i279\"]")


    # step monitor
    stepMonitorYes     = driver.find_element_by_xpath("//*[@id=\"i286\"]")
    stepMonitorNo      = driver.find_element_by_xpath("//*[@id=\"i289\"]")

    genderArray        = [genderMale, genderFemale, genderOther]
    stepMonitorArray   = [stepMonitorYes, stepMonitorNo]
    lifestyleArray     = [lifestyleHealthy, lifestyleUnhealthy, lifestyleModeratelyHealthy, lifestyleCantSay]
    spentArray         = [spentLot, spentFareAmmount, spentLess, spentNeverConsidered]
    metabolismArray    = [metabolismFast, metabolismSlow, metabolismModerate, metabolismDontKnow]
    diseaseArray       = [diseaseHeart, diseaseAbdomen, diseaseAllergies, diseaseOther]
    preferFoodArray    = [preferJunk, preferHealthy, preferFare, preferNeverConsidered]
    stressEatJunkArray = [StressEatJunkFoodYes, StressEatJunkFoodSometimes, StressEatJunkFoodRarely, StressEatJunkFoodNever]
    workoutTypeArray   = [workoutTypeGym, workoutTypeRunning, workoutTypeWaling, workoutTypeJogging, workoutTypeCycling,
                        workoutTypeCardio, workoutTypeNoWorkout]
    workoutArray       = [workoutDaily, workoutAlternateDays, workoutOnceInWeek, workoutFewTimesInMonth, workoutRarely, workoutNever]
    junkArray          = [junkDaily, junkAlternateDays, junkOnceInWeek, junkFewTimesInMonth, junkRarely, junkNever]
    mealArray          = [mealInDayTwo, mealInDayThree, mealInDayFour, mealInDayFive]
    occupationArray    = [occupationOfficeJob, occupationFieldJob, occupationBusinessJob, occupationStudentJob, occupationNotWorkingJob]
    smokeArray         = [smokeDaily, smokeAlternateDays, smokeOnceInWeek, smokeFewTimesInMonth, smokeRarely, smokeNever]
    alcoholArray       = [alcoholDaily, alcoholAlternateDays, alcoholOnceInWeek, alcoholFewTimesInMonth, alcoholRarely, alcoholNever]

    cityList =  ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana"	,
                 "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
                 "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
                 "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    #  form fields
    randomName = names.get_full_name()
    randomAgeArray = [21, 22, 23, 24, 25, 26, 26, 28, 29, 30] # first 21 - 30 age
    randomWeight = random.randint(45, 100)
    randomHeight = random.randint(145, 210)
    randomDisease = random.randint(1, 4)

    sleepTime = 0.1
    formCount = 1
    i = 0
    while i < formCount:
        try:
            # fill form
            # name
            time.sleep(2)
            personName.send_keys(randomName)
            time.sleep(sleepTime)

            # Age
            age.send_keys(random.choice(randomAgeArray))
            time.sleep(sleepTime)

            # gender
            random.choice(genderArray).click()
            time.sleep(sleepTime)

            # weight
            weight.send_keys(randomWeight)
            time.sleep(sleepTime)

            # Height
            height.send_keys(randomHeight)
            time.sleep(sleepTime)

            # city name
            city.send_keys("Delhi")
            time.sleep(sleepTime)

            # occupation
            random.choice(occupationArray).click()
            time.sleep(sleepTime)


            #smoke
            random.choice(smokeArray).click()
            time.sleep(sleepTime)

            # alcohol
            random.choice(alcoholArray).click()
            time.sleep(sleepTime)

            # meal
            random.choice(mealArray).click()
            time.sleep(sleepTime)

            # eat junk
            random.choice(junkArray).click()
            time.sleep(sleepTime)


            # workout
            workout = random.choice(workoutArray)
            workout.click()
            # type of workout
            if workout == workoutNever:
                workoutTypeArray[-1].click()
            else:
                random.choice(workoutTypeArray).click()

            time.sleep(sleepTime)



            # stress junk eating
            random.choice(stressEatJunkArray).click()
            time.sleep(sleepTime)

            # eating preference
            random.choice(preferFoodArray).click()
            time.sleep(sleepTime)


            # disease
            for i in range(randomDisease):
                random.choice(diseaseArray).click()
                time.sleep(sleepTime)

            # metabolism
            random.choice(metabolismArray).click()
            time.sleep(sleepTime)


            # spent on junk
            random.choice(spentArray).click()
            time.sleep(sleepTime)

            # lifestyle
            random.choice(lifestyleArray).click()
            time.sleep(sleepTime)

            # monitor steps
            random.choice(stepMonitorArray).click()
            time.sleep(sleepTime)

        except:
            continue

        i+=1


getInputs()