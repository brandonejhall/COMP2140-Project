<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="index.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <title>Document</title>
</head>
<body>
    <?php include 'assets/php/header.php';?>
    
    <div class="body1">
        <div id="body-head">
            <h1>Placement and Career Services</h1>
            
        </div>
        <div class="form-group">
            <div id="contents">
                <h2>Career Services Form</h2>
                <form action="" id="myform" method="post">
                    <fieldset>
                        <div class="form-input">
                            <label for="name">Enter Name: <em>(Required)</em></label>
                            <input type="name" id="name" placeholder="eg. John Doe" require>
                        </div>
                        <div class="form-input">
                            <label for="id">Enter ID#: <em>(Required)</label>
                            <input type="id" id="id" placeholder="eg. 123456789" require>
                        </div>
                        <div class="form-input">
                            <label for="email">Enter Email: <em>(Required)</label>
                            <input type="email" id="email" placeholder="eg. johndoe@mymona.uwi.edu" require>
                        </div>    
                        <div class="form-input">
                            <label for="reason">Reason: <em>(Required)</label>
                            <select class="form-control" name="reason" id="reason" require>
                                <option value="Individual Career Counselling">Individual Career Counselling</option>
                                <option value="Career Protfolio Guidance">Career Protfolio Guidance</option>
                                <option value="Resume Advising/Reviews">Resume Advising/Reviews</option>
                                <option value="Cover Letter Advising Reviews">Cover Letter Advising Reviews</option>
                                <option value="Job Interview Techniques Coaching">Job Interview Techniques Coaching</option>
                                <option value="Job Search Assistance">Job Search Assistance</option>
                                <option value="Job Referrals-Summer/Part-Time/Full-Time">Job Referrals-Summer/Part-Time/Full-Time</option>
                                <option value="Internship Coordination">Internship Coordination</option>
                                <option value="Employment Compensation Package Advising">Employment Compensation Package Advising</option>
                                <option value="Career Explorations Opportunities">Career Explorations Opportunities</option>
                                <option value="Career Development/World of Work Seminars">Career Development/World of Work Seminars</option>
                                <option value="Overseas Work & Travel Programme">Overseas Work & Travel Programme</option>

                            </select>
                        </div>      
                    </fieldset> 
                </form>                 
            </div>  
            <div class="form-button">
                <button id="form-submit">Submit</button>
            </div>               
        </div>
        
    </div>
    <?php include 'assets/php/footer.php';?>
    
</body>
</html>