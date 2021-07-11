# Load your usual SpaCy model (one of SpaCy English models)
import spacy
# nlp = spacy.load('en_core_web_sm')
import ipdb;ipdb.set_trace()
nlp = spacy.load('en')

# load NeuralCoref and add it to the pipe of SpaCy's model
import neuralcoref
coref = neuralcoref.NeuralCoref(nlp.vocab)
nlp.add_pipe(coref, name='neuralcoref')

# You're done. You can now use NeuralCoref the same way you usually manipulate a SpaCy document and it's annotations.
# doc = nlp(u'My sister has a dog. She loves him.')
doc = nlp(u'The sole published decision of this court that has dealt with the issues now before us is Lennon v. Metropolitan Life Insurance Co., 504 F.3d 617 (6th Cir. 2007). That case involved what the court described as "grossly negligent," "reckless drunk driving," id. at 618, 624, and resulted in three separate opinions — a lead, a concurrence, and a dissent. Lennon was insured under an ERISA-covered personal accident insurance (PAI) policy. On the day in question, he drove his car at a high rate of speed the wrong way down a one-way portion of a divided street, losing control of his vehicle. The car hit a curb, flew into the air, and slammed into a brick wall, killing Lennon. Lennon\'s BAC was later measured at .321, more than three times the legal limit in effect at the time (.10) and high enough to render him only semi-conscious. See Blood Alcohol Levels and Metabolism, http://www.radford.edu/kcastleb/bac.html. Death has [**6] been documented to occur at BACs starting at .35. Id.Lennon\'s PAI policy provided in pertinent part as follows:If, while insured for Personal Accident Insurance, an [insured] sustains accidental bodily injuries, and within one year thereafter shall have suffered loss of life . . . as a direct result of such bodily injuries independently of all other causes, [MetLife] shall pay the benefit specified for such Losses. Lennon, 504 F.3d at 619 (alterations in original). MetLife denied benefits to Lennon\'s estate, noting in its denial letter that Lennon\'s BAC was three times the legal limit and that "[t]he act of driving impaired . . . rendered the infliction of serious injury or death reasonably foreseeable and, hence, not accidental." Id. at 620. It thus concluded that Lennon\'s death was not "directly the result of accidental injuries, independent[] of all other causes." Id. The lead opinion concluded that MetLife had not acted arbitrarily and capriciously in denying coverage for Lennon\'s death. Id. at 620-21. Borrowing terminology from tort law, the lead opinion characterized Lennon\'s behavior as "grossly negligent." Id. at 621. It therefore reasoned that "in extreme cases courts may treat wanton misconduct more like an intentional tort than like negligence[,]" id. (quoting Dan R. Dobbs, The Law of Torts § 147, at 350-51 (2000)), and that a plan administrator could similarly "treat such conduct as not accidental under a policy that only covers accidents." Lennon, 504 F.3d at 621. The lead Lennon opinion also stated that the number of cases holding that drunk driving wrecks are not accidents "independently supports the conclusion that MetLife\'s determination was not arbitrary and capricious." Id. at 622-23 (collecting cases).')
# doc = nlp(u'We review de novo the district court\'s disposition of an ERISA action based upon the administrative record, and apply the same legal standard as the district court. Wilkins v. Baptist Healthcare Sys., Inc., 150 F.3d 609, 613 (6th Cir. 1998). As discussed in Part II.B. below, the district court in this case appropriately reviewed the Kovaches\' suit under the arbitrary-and-capricious standard because the Plan granted discretionary authority to Zurich as the plan administrator to interpret the Plan\'s terms and to determine its benefits. See Firestone Tire & Rubber Co. v. Bruch, 489 U.S. 101, 111-15, 109 S.Ct. 948, 103 L.Ed.2d 80 (1989) (establishing the arbitrary-and-capricious standard of review in ERISA cases where the plan administrator has discretionary authority); [**4] Glenn v. MetLife. Ins. Co., 461 F.3d 660, 666 (6th Cir. 2006) (applying Firestone\'s standard of review).')

hc = doc._.has_coref
crfc = doc._.coref_clusters

print('has_coref')
print(hc)
print('coref_clusters')
print(crfc)
