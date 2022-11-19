{% extends 'base.html' %}

{% block title %}

<title>Hire-Up</title>

{% endblock %}

{% block content %}
<div class="container">

<h1>Edit </h1>

<form action="/hr/openings/edit/{{data[0]}}" method="POST" class="form-control">

    <label for="exampleInputEmail1" class="form-label">Title</label>
    
    <input type="text" class="form-control "name="title" value="{{data[1]}}">
    <div id="emailHelp" class="form-text">i.e Python developer,nodejs developer</div>   
  

  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Company Name</label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="company_name"value="{{data[2]}}">
  </div>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Designation</label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="designation" value="{{data[3]}}">
  </div>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Salary Range</label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="salary_range" value="{{data[4]}}">
    <div id="emailHelp" class="form-text">i.e 5-7 lpa,12-15 lpa</div> 
  </div>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Skills required</label>
    <input type="text" class="form-control" name="skills_required" value="{{data[5]}}">
    <div id="emailHelp" class="form-text">i.e Python,Nodejs</div> 
  </div>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Roles and Responsibilities</label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="roles_responsibilities" value="{{data[6]}}">
    <div id="emailHelp" class="form-text">Write each Responsibilities with comma separated</div> 
  </div>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Company Description</label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="company_description" value="{{data[7]}}">
  </div>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Location</label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="location" value="{{data[8]}}">
  </div>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Website</label>
    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="website" value="{{data[9]}}"">
  </div>

<button class="btn btn-success" type="submit" >Save</button>
</form>
</div>




</div>

{% endblock %}
